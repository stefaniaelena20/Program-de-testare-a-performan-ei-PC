import time  # masurarea precisa a timpului de executie
import platform
import psutil  # specificatii hard
import sys
import cpuinfo  # specificatii hard
import random
from datetime import datetime
import tkinter as tk  # gui
from tkinter import ttk, scrolledtext
from threading import Thread  # ruleaza testele in fundal


class PerformanceTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Testare Performanță PC - Czebely Stefania-Elena")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f4f8')

        self.results = {}
        self.create_widgets()

    def create_widgets(self):

        header_frame = tk.Frame(self.root, bg='#4f46e5', pady=20)
        header_frame.pack(fill='x')

        title = tk.Label(header_frame, text="Program Testare Performanță PC",
                         font=('Arial', 24, 'bold'), bg='#4f46e5', fg='white')
        title.pack()

        subtitle = tk.Label(header_frame, text="Czebely Stefania-Elena",
                            font=('Arial', 12), bg='#4f46e5', fg='white')
        subtitle.pack()

        date_label = tk.Label(header_frame,
                              text=f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} | {platform.system()} {platform.release()}",
                              font=('Arial', 10), bg='#4f46e5', fg='white')
        date_label.pack(pady=5)


        main_container = tk.Frame(self.root, bg='#f0f4f8')
        main_container.pack(fill='both', expand=True, padx=20, pady=20)


        left_panel = tk.Frame(main_container, bg='white', relief='solid', borderwidth=1)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))

        button_title = tk.Label(left_panel, text="Teste Disponibile",
                                font=('Arial', 16, 'bold'), bg='white', fg='#1f2937')
        button_title.pack(pady=15)


        self.buttons = {}

        # BUTOANELE DEFINITE PENTRU TESTARE (DOAR CELE 7 CERUTE)
        tests = [
            ("cpu_info", "🖥️ Informații Procesor", self.test_cpu_info),
            ("memory_info", "💾 Informații Memorie", self.test_memory_info),
            ("mem_access", "⚡ Test Timp Acces Memorie", self.test_memory_access),
            ("mem_transfer", "📊 Test Viteză Transfer Memorie", self.test_memory_transfer),
            ("int_ops", "🔢 Test Operații Întregi", self.test_integer_operations),
            ("float_ops", "📐 Test Operații Flotante", self.test_float_operations),
            ("mandelbrot", "🎨 Test Mandelbrot", self.test_mandelbrot),
        ]

        # FACE BUTOANELE VIZUALE
        for key, text, command in tests:
            btn = tk.Button(left_panel, text=text, command=lambda c=command, k=key: self.run_test(c, k),
                            font=('Arial', 11), bg='#e5e7eb', fg='#1f2937',
                            relief='flat', cursor='hand2', pady=10, anchor='w', padx=20)
            btn.pack(fill='x', padx=15, pady=5)
            self.buttons[key] = btn


        action_frame = tk.Frame(left_panel, bg='white')
        action_frame.pack(fill='x', padx=15, pady=15)

        self.calc_btn = tk.Button(action_frame, text="🏆 Calculează Scor Final",
                                  command=self.calculate_score,
                                  font=('Arial', 12, 'bold'), bg='#4f46e5', fg='white',
                                  relief='flat', cursor='hand2', pady=12)
        self.calc_btn.pack(fill='x', pady=5)

        reset_btn = tk.Button(action_frame, text="🔄 Reset Toate Testele",
                              command=self.reset_all,
                              font=('Arial', 11), bg='#6b7280', fg='white',
                              relief='flat', cursor='hand2', pady=10)
        reset_btn.pack(fill='x')


        right_panel = tk.Frame(main_container, bg='white', relief='solid', borderwidth=1)
        right_panel.pack(side='right', fill='both', expand=True)

        results_title = tk.Label(right_panel, text="Rezultate Teste",
                                 font=('Arial', 16, 'bold'), bg='white', fg='#1f2937')
        results_title.pack(pady=15)


        self.results_text = scrolledtext.ScrolledText(right_panel, wrap=tk.WORD,
                                                      font=('Courier', 10),
                                                      bg='#f9fafb', fg='#1f2937',
                                                      relief='flat', padx=15, pady=15)
        self.results_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))

    def run_test(self, test_func, key):
        """Rulează un test într-un thread separat"""
        self.buttons[key].config(bg='#60a5fa', text=f"⏳ Rulează...", state='disabled')
        self.root.update()

        def run():
            test_func()
            self.buttons[key].config(bg='#10b981', text=f"✓ {self.buttons[key]['text'].split(' ', 1)[1]}",
                                     state='normal')

        Thread(target=run, daemon=True).start()

    def add_result(self, title, content):
        """Adaugă rezultate în zona de text"""
        self.results_text.insert(tk.END, f"\n{'=' * 60}\n")
        self.results_text.insert(tk.END, f"  {title}\n")
        self.results_text.insert(tk.END, f"{'=' * 60}\n")
        self.results_text.insert(tk.END, content + "\n")
        self.results_text.see(tk.END)

    # Informații Procesor
    def test_cpu_info(self):

        info = cpuinfo.get_cpu_info()

        content = f"Producător: {info.get('vendor_id_raw', 'N/A')}\n"
        content += f"Brand: {info.get('brand_raw', 'N/A')}\n"
        content += f"Arhitectură: {info.get('arch', 'N/A')}\n"
        content += f"Număr de biți: {info.get('bits', 'N/A')}\n"
        content += f"Nuclee fizice: {psutil.cpu_count(logical=False)}\n"
        content += f"Nuclee logice: {psutil.cpu_count(logical=True)}\n"

        freq = psutil.cpu_freq()
        if freq:
            content += f"Frecvență maximă: {freq.max:.2f} MHz\n"
            content += f"Frecvență curentă: {freq.current:.2f} MHz\n"

        self.results['cpu_info'] = info
        self.add_result("INFORMAȚII PROCESOR", content)

    # Informații Memorie
    def test_memory_info(self):

        mem = psutil.virtual_memory()

        content = f"Memorie totală: {mem.total / (1024 ** 3):.2f} GB\n"
        content += f"Memorie disponibilă: {mem.available / (1024 ** 3):.2f} GB\n"
        content += f"Memorie utilizată: {mem.used / (1024 ** 3):.2f} GB\n"
        content += f"Procentaj utilizare: {mem.percent}%\n"

        self.results['memory_info'] = mem
        self.add_result("INFORMAȚII MEMORIE", content)

    # Test Timp Acces Memorie
    def test_memory_access(self):

        size = 10_000_000
        test_array = list(range(size))

        # Acces secvențial
        start = time.perf_counter()
        total = 0
        for i in range(0, size, 100):
            total += test_array[i]
        elapsed = time.perf_counter() - start
        seq_time = (elapsed / (size / 100)) * 1_000_000_000

        # Acces aleatoriu
        indices = [random.randint(0, size - 1) for _ in range(100_000)]
        start = time.perf_counter()
        total = 0
        for idx in indices:
            total += test_array[idx]
        elapsed = time.perf_counter() - start
        rand_time = (elapsed / len(indices)) * 1_000_000_000

        content = f"Timp mediu acces secvențial: {seq_time:.2f} ns\n"
        content += f"Timp mediu acces aleatoriu: {rand_time:.2f} ns\n"

        self.results['mem_access'] = {'seq': seq_time, 'rand': rand_time}
        self.add_result("TEST TIMP ACCES MEMORIE", content)

    # Test Viteză Transfer Memorie
    def test_memory_transfer(self):

        sizes = [1024, 10240, 102400, 1024000]
        speeds = []
        content = ""

        for size in sizes:
            data = bytearray(size)
            iterations = max(1000, 100_000_000 // size)

            start = time.perf_counter()
            for _ in range(iterations):
                temp = data[:]
            elapsed = time.perf_counter() - start

            total_mb = (size * iterations) / (1024 * 1024)
            speed = total_mb / elapsed
            speeds.append(speed)

            size_str = f"{size / 1024:.1f} KB" if size < 1024000 else f"{size / 1024000:.1f} MB"
            content += f"Bloc {size_str:>8}: {speed:>10.2f} MB/s\n"

        avg_speed = sum(speeds) / len(speeds)
        content += f"\nViteză medie: {avg_speed:.2f} MB/s"

        self.results['mem_transfer'] = avg_speed
        self.add_result("TEST VITEZĂ TRANSFER MEMORIE", content)

    # Test Operații Întregi
    def test_integer_operations(self):

        iterations = 10_000_000
        results = {}
        content = ""

        # Adunare
        start = time.perf_counter()
        result = 0
        for i in range(iterations):
            result += i
        elapsed = time.perf_counter() - start
        ops = iterations / elapsed
        results['add'] = ops
        content += f"Adunare:    {ops / 1_000_000:>8.2f} MOPS\n"

        # Înmulțire
        start = time.perf_counter()
        result = 1
        for i in range(1, iterations // 100):
            result = (result * i) % 1_000_000
        elapsed = time.perf_counter() - start
        ops = (iterations // 100) / elapsed
        results['mul'] = ops
        content += f"Înmulțire:  {ops / 1_000_000:>8.2f} MOPS\n"

        self.results['int_ops'] = results
        self.add_result("TEST OPERAȚII ÎNTREGI", content)

    # Test Operații Flotante
    def test_float_operations(self):

        iterations = 1_000_000
        results = {}
        content = ""

        # Adunare
        start = time.perf_counter()
        result = 0.0
        for i in range(iterations):
            result += float(i) * 0.5
        elapsed = time.perf_counter() - start
        ops = iterations / elapsed
        results['add'] = ops
        content += f"Adunare:    {ops / 1_000_000:>8.2f} MFLOPS\n"

        # Înmulțire
        start = time.perf_counter()
        result = 1.0
        for i in range(iterations):
            result = (result * 1.0000001) % 1000.0
        elapsed = time.perf_counter() - start
        ops = iterations / elapsed
        results['mul'] = ops
        content += f"Înmulțire:  {ops / 1_000_000:>8.2f} MFLOPS\n"

        self.results['float_ops'] = results
        self.add_result("TEST OPERAȚII FLOTANTE", content)

    # Test Mandelbrot
    def test_mandelbrot(self):


        def mandelbrot(c, max_iter=100):
            z = 0
            for n in range(max_iter):
                if abs(z) > 2:
                    return n
                z = z * z + c
            return max_iter

        width, height = 400, 400
        start = time.perf_counter()
        points = 0

        for x in range(width):
            for y in range(height):
                c = complex(-2.0 + (x / width) * 3.0, -1.5 + (y / height) * 3.0)
                mandelbrot(c)
                points += 1

        elapsed = time.perf_counter() - start
        perf = points / elapsed

        content = f"Puncte calculate: {points:,}\n"
        content += f"Timp total: {elapsed:.2f} secunde\n"
        content += f"Performanță: {perf / 1_000_000:.2f} MP/s\n"

        self.results['mandelbrot'] = perf
        self.add_result("TEST MANDELBROT", content)

    def calculate_score(self):
        """Calculează scorul final"""
        # Verifică doar testele rămase în listă
        required = ['int_ops', 'float_ops', 'mandelbrot', 'mem_transfer']

        if not all(key in self.results for key in required):
            self.add_result("EROARE", "Rulați toate testele înainte de a calcula scorul!")
            return

        # Referințe
        ref_int = 50_000_000
        ref_float = 20_000_000
        ref_mandelbrot = 100_000
        ref_mem = 1000

        # Calcul scoruri
        score_int = (self.results['int_ops']['add'] / ref_int) * 100
        score_float = (self.results['float_ops']['add'] / ref_float) * 100
        score_mandelbrot = (self.results['mandelbrot'] / ref_mandelbrot) * 100
        score_mem = (self.results['mem_transfer'] / ref_mem) * 100

        total = (score_int * 0.25 + score_float * 0.25 + score_mandelbrot * 0.25 +
                 score_mem * 0.25)

        # Evaluare
        if total >= 150:
            rating = "EXCELENT - Performanță superioară"
        elif total >= 100:
            rating = "FOARTE BUN - Performanță peste medie"
        elif total >= 70:
            rating = "BUN - Performanță medie"
        elif total >= 50:
            rating = "SATISFĂCĂTOR - Performanță sub medie"
        else:
            rating = "SLAB - Performanță redusă"

        content = f"Scor operații întregi:    {score_int:>6.1f} / 100\n"
        content += f"Scor operații flotante:   {score_float:>6.1f} / 100\n"
        content += f"Scor Mandelbrot:          {score_mandelbrot:>6.1f} / 100\n"
        content += f"Scor viteză memorie:      {score_mem:>6.1f} / 100\n"
        content += f"\n{'=' * 60}\n"
        content += f"SCOR TOTAL:               {total:>6.1f} / 100\n"
        content += f"{'=' * 60}\n"
        content += f"Evaluare: {rating}\n"

        self.add_result("🏆 EVALUARE GLOBALĂ PERFORMANȚĂ", content)

    def reset_all(self):
        """Resetează toate testele"""
        self.results = {}
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Rezultatele vor apărea aici după rularea testelor...\n")

        for key, btn in self.buttons.items():
            original_text = btn['text'].split(' ', 1)[-1] if '✓' in btn['text'] else btn['text'].split(' ', 1)[-1]
            btn.config(bg='#e5e7eb', text=f"{btn['text'].split()[0]} {original_text}", state='normal')


def main():
    root = tk.Tk()
    app = PerformanceTestGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()