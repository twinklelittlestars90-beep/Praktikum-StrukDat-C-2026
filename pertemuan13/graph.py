class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f"[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)")

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota in self.graph:
            print(f"- {kota} terhubung ke: ", end="")
            for tetangga, jarak in self.graph[kota]:
                print(f"{tetangga} ({jarak}) ", end="")
            print()

    def dijkstra(self, start):
        print(f"\n[PROSES] Menghitung rute terpendek dari: {start}...\n")
        jarak = {}
        dikunjungi = {}
        for kota in self.graph:
            jarak[kota] = float('inf')
            dikunjungi[kota] = False
        jarak[start] = 0

        for _ in range(len(self.graph)):
            min_node = None
            min_value = float('inf')

            for kota in self.graph:
                if not dikunjungi[kota] and jarak[kota] < min_value:
                    min_value = jarak[kota]
                    min_node = kota

            if min_node is None:
                break

            dikunjungi[min_node] = True

            for tetangga, bobot in self.graph[min_node]:
                if not dikunjungi[tetangga]:
                    if jarak[min_node] + bobot < jarak[tetangga]:
                        jarak[tetangga] = jarak[min_node] + bobot

        print("[HASIL] Jarak Terpendek dari Jakarta:")
        for kota in jarak:
            print(f"- Ke {kota}: {jarak[kota]} km")

        print("\n=========================================")
        print("Simulasi Navigasi Selesai!")


g = Graph()
print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU" \n=========================================')
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)
g.tampilkan_graph()
g.dijkstra("Jakarta")