# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    

    def cargar_datos():
        # Creamos la carpeta docs
        docs = Path('docs')
        docs.mkdir(parents=True, exist_ok=True)

        #Leemos el dataframe
        df = pd.read_csv('files/input/shipping-data.csv', index_col=0)

        return df
    
    
    def create_visual_for_shipping_per_warehouse(df):
        """
        Crea el grafico de barra que hace el conteo de cantidad de
        registros por cada almacen y lo guarda en la carpeta docs.
        """
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title='Shipping per Warehouse',
            xlabel='Warehouse block',
            ylabel='Record count',
            color='tab:blue',
            fontsize=8
        )
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.savefig('docs/shipping_per_warehouse.png')


    def create_visual_for_mode_of_shipment(df):
        """
        Crea el grafico de torta del conteo de registros
        por modo de envio y lo guarda en la carpeta docs.
        """
        df = df.copy()
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"]
        )
        plt.savefig("docs/mode_of_shipment.png")

    
    def create_visual_for_average_customer_rating(df):
        """
        Crea el grafico de barra modificado del promedio de los
        registros por modo de envio y lo guarda en la carpeta docs.
        """
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df = df[["mean", "min", "max"]]
        plt.barh(
            y=df.index.values,
            width=df["max"].values - 1,
            left=df["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors = [
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]
        plt.barh(
            y=df.index.values,
            width=df["mean"].values - 1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        
        plt.savefig("docs/average_customer_rating.png")

    
    def create_visual_for_weight_distribution(df):
        """
        Crea el histograma de los registros en la columna de
        pesos por gramo y lo guarda en la carpeta docs.
        """
        df = df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white"
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/weight_distribution.png")
    

    def crear_dashboard_html():
        # El contenido HTML es la cadena de texto multilínea que quieres escribir.
        html_content = """
            <!DOCTYPE html>
            <html>
            <body>

            <h1>Shipping Dashboard Example</h1>
            <div style="width:45%;float:left">
                <img src="shipping_per_warehouse.png" alt="Fig 1">
                <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%;float:left">
                <img src="average_customer_rating.png" alt="Fig 3">
                <img src="weight_distribution.png" alt="Fig 4">
            </div>

            </body>
            </html>
        """
        try:
            with open('docs/index.html', 'w') as f:
                f.write(html_content.strip())
            print("✅ Archivo 'index.html' creado exitosamente.")
        except Exception as e:
            print(f"❌ Error al escribir el archivo: {e}")

    
    # Cargamos los datos y creamos la carpeta 'docs'
    df = cargar_datos()

    # Llamamos las funciones para crear los graficos
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    # Creamos nuestro dashboard html
    crear_dashboard_html()