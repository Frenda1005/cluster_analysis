import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
import os

class ClusterAnalysisApp:
    def __init__(self, master):
        self.master = master
        master.title("Cluster Analysis App")

        self.label = Label(master, text="Cluster Analysis")
        self.label.pack()

        self.upload_button = Button(master, text="Upload CSV", command=self.upload_file)
        self.upload_button.pack()

        self.elbow_button = Button(master, text="Define Cluster Number", command=self.define_cluster_number)
        self.elbow_button.pack()

        self.cluster_label = Label(master, text="Enter Cluster Number:")
        self.cluster_label.pack()

        self.cluster_entry = Entry(master)
        self.cluster_entry.pack()

        self.analyze_button = Button(master, text="Analyze", command=self.analyze_clusters)
        self.analyze_button.pack()

        self.file_path = None
        self.output_dir = None

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")
        else:
            messagebox.showwarning("No File", "Please select a CSV file")

    def define_cluster_number(self):
        if not self.file_path:
            messagebox.showwarning("No File", "Please upload a CSV file first")
            return

        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            messagebox.showwarning("No Directory", "Please select an output directory")
            return

        # Create a subdirectory named 'cluster_result' within the chosen directory
        self.output_dir = os.path.join(self.output_dir, 'cluster_result')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        data = pd.read_csv(self.file_path)
        features = data.columns[1:]
        X = data[features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        wcss = []
        silhouette_scores = []
        K = range(2, 8)

        for k in K:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X_scaled)
            wcss.append(kmeans.inertia_)

            clusters = kmeans.labels_
            silhouette_avg = silhouette_score(X_scaled, clusters)
            silhouette_scores.append(silhouette_avg)

        plt.figure(figsize=(10, 5))
        plt.plot(K, wcss, 'bx-')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('WCSS')
        plt.title('Elbow Method for Optimal k')
        plt.savefig(os.path.join(self.output_dir, 'elbow_method.png'))
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(K, silhouette_scores, 'bx-')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Score for Optimal k')
        plt.savefig(os.path.join(self.output_dir, 'silhouette_score.png'))
        plt.close()

        messagebox.showinfo("Cluster Number", "Please check the saved plots and enter the desired cluster number")

    def analyze_clusters(self):
        if not self.file_path:
            messagebox.showwarning("No File", "Please upload a CSV file first")
            return

        if not self.output_dir:
            messagebox.showwarning("No Directory", "Please define the cluster number and select the output directory first")
            return

        try:
            optimal_k = int(self.cluster_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for clusters")
            return

        data = pd.read_csv(self.file_path)
        features = data.columns[1:]
        X = data[features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)

        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        clusters = kmeans.fit_predict(X_pca)

        data['Cluster'] = clusters

        plt.figure(figsize=(8, 6))
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.title('K-Means Clustering of Constructs')
        plt.colorbar()
        plt.savefig(os.path.join(self.output_dir, 'kmeans_clustering.png'))
        plt.close()

        clustered_data = data.groupby('Cluster').mean()
        clustered_data_file_path = os.path.join(self.output_dir, 'cluster_centers.csv')
        clustered_data.to_csv(clustered_data_file_path)

        for feature in features:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='Cluster', y=feature, data=data)
            plt.title(f'Distribution of {feature} by Cluster')
            plt.savefig(os.path.join(self.output_dir, f'{feature}_distribution.png'))
            plt.close()

        output_file_path = os.path.join(self.output_dir, 'clusters.csv')
        data.to_csv(output_file_path, index=False)
        messagebox.showinfo("Output File", f"Clustered data saved to {output_file_path}")

if __name__ == "__main__":
    root = Tk()
    app = ClusterAnalysisApp(root)
    root.mainloop()
