import tkinter as tk
from tkinter import ttk, messagebox

GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

PENYAKIT = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nasofaring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"],
}


class ExpertSystemTHT:
    def __init__(self, gejala_db, penyakit_db):
        self.gejala_db = gejala_db
        self.penyakit_db = penyakit_db

    def diagnose(self, selected_gejala):
        if not selected_gejala:
            return []

        results = []
        selected_set = set(selected_gejala)

        for nama_penyakit, daftar_gejala in self.penyakit_db.items():
            aturan_set = set(daftar_gejala)
            cocok = selected_set.intersection(aturan_set)

            skor = len(cocok)
            persentase = (skor / len(aturan_set)) * 100

            if skor > 0:
                results.append({
                    "penyakit": nama_penyakit,
                    "skor": skor,
                    "total_gejala_penyakit": len(aturan_set),
                    "persentase": persentase,
                    "gejala_cocok": sorted(list(cocok), key=lambda x: int(x[1:])),
                    "gejala_tidak_cocok": sorted(list(aturan_set - selected_set), key=lambda x: int(x[1:])),
                })

        results.sort(key=lambda x: (-x["persentase"], -x["skor"], x["penyakit"]))
        return results


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Pakar Diagnosa Penyakit THT")
        self.geometry("980x700")
        self.resizable(True, True)

        self.expert_system = ExpertSystemTHT(GEJALA, PENYAKIT)
        self.check_vars = {}

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self,
            text="Sistem Pakar Diagnosa Penyakit THT",
            font=("Arial", 18, "bold"),
            pady=10,
        )
        title.pack()

        subtitle = tk.Label(
            self,
            text="Pilih gejala yang dialami pasien, lalu klik tombol Diagnosa",
            font=("Arial", 11),
        )
        subtitle.pack(pady=(0, 10))

        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=12, pady=8)

        left_frame = tk.LabelFrame(main_frame, text="Daftar Gejala", padx=10, pady=10)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

        right_frame = tk.LabelFrame(main_frame, text="Hasil Diagnosa", padx=10, pady=10)
        right_frame.pack(side="right", fill="both", expand=True)

        # Scrollable checkbox area
        canvas = tk.Canvas(left_frame)
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for i, (kode, nama) in enumerate(GEJALA.items()):
            var = tk.BooleanVar()
            self.check_vars[kode] = var
            cb = tk.Checkbutton(
                scrollable_frame,
                text=f"{kode} - {nama}",
                variable=var,
                anchor="w",
                justify="left",
                font=("Arial", 10),
            )
            cb.grid(row=i, column=0, sticky="w", pady=2)

        # Tombol aksi
        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(fill="x", pady=(10, 0))

        diagnosa_btn = tk.Button(
            btn_frame,
            text="Diagnosa",
            font=("Arial", 11, "bold"),
            command=self.run_diagnosis,
            width=15,
        )
        diagnosa_btn.pack(side="left", padx=(0, 6))

        reset_btn = tk.Button(
            btn_frame,
            text="Reset",
            font=("Arial", 11),
            command=self.reset_form,
            width=15,
        )
        reset_btn.pack(side="left")

        # Output area
        self.result_text = tk.Text(right_frame, wrap="word", font=("Consolas", 10))
        self.result_text.pack(fill="both", expand=True)

        self.result_text.insert(
            "1.0",
            "Hasil diagnosa akan tampil di sini.\n"
            "\n"
            "Catatan:\n"
            "- Sistem membandingkan gejala yang dipilih dengan basis pengetahuan.\n"
            "- Penyakit dengan persentase kecocokan tertinggi ditampilkan paling atas.\n"
            "- Ini hanya simulasi sistem pakar untuk keperluan praktikum.\n"
        )
        self.result_text.config(state="disabled")

    def get_selected_gejala(self):
        return [kode for kode, var in self.check_vars.items() if var.get()]

    def run_diagnosis(self):
        selected = self.get_selected_gejala()

        if not selected:
            messagebox.showwarning("Peringatan", "Pilih minimal satu gejala terlebih dahulu.")
            return

        hasil = self.expert_system.diagnose(selected)
        self.show_results(selected, hasil)

    def show_results(self, selected, hasil):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        self.result_text.insert(tk.END, "GEJALA YANG DIPILIH:\n")
        for kode in sorted(selected, key=lambda x: int(x[1:])):
            self.result_text.insert(tk.END, f"- {kode} : {GEJALA[kode]}\n")

        self.result_text.insert(tk.END, "\n")

        if not hasil:
            self.result_text.insert(tk.END, "Tidak ditemukan penyakit yang cocok.\n")
            self.result_text.config(state="disabled")
            return

        terbaik = hasil[0]
        self.result_text.insert(tk.END, "HASIL DIAGNOSA UTAMA:\n")
        self.result_text.insert(
            tk.END,
            f"{terbaik['penyakit']}\n"
            f"Kecocokan: {terbaik['persentase']:.2f}% ({terbaik['skor']} dari {terbaik['total_gejala_penyakit']} gejala)\n"
        )
        self.result_text.insert(tk.END, "Gejala yang cocok:\n")
        for kode in terbaik["gejala_cocok"]:
            self.result_text.insert(tk.END, f"  * {kode} - {GEJALA[kode]}\n")

        self.result_text.insert(tk.END, "\nRANKING SEMUA KEMUNGKINAN:\n")
        for i, item in enumerate(hasil, start=1):
            self.result_text.insert(
                tk.END,
                f"{i}. {item['penyakit']} -> {item['persentase']:.2f}% "
                f"({item['skor']}/{item['total_gejala_penyakit']} gejala cocok)\n"
            )

        self.result_text.insert(
            tk.END,
            "\nKESIMPULAN:\n"
            "Penyakit dengan nilai kecocokan tertinggi dianggap sebagai diagnosa paling mungkin berdasarkan data pada modul.\n"
        )

        self.result_text.config(state="disabled")

    def reset_form(self):
        for var in self.check_vars.values():
            var.set(False)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(
            "1.0",
            "Form berhasil direset.\n\nSilakan pilih gejala lalu klik Diagnosa."
        )
        self.result_text.config(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
