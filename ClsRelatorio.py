from fpdf import FPDF
from datetime import date, datetime


class Relatorio:
    def __init__(self, informacoes, resultado: dict):
        self.today = date.today()
        self.now = datetime.now()
        self.now = str(self.now.hour) + "-" + str(self.now.minute) + "-" + str(self.now.second)
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')
        self.n_informacoes = informacoes
        self.resultadoFinal = resultado
        self.nome_arquivo = str(self.today) + str(self.now)

    def criaPDF(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=15)
        self.pdf.multi_cell(200, 10, txt="{}\n {}".format(self.today.strftime("%d/%m/%Y"), self.now), align="L")
        self.pdf.set_font("Arial", size=30)
        self.pdf.image('https://raw.githubusercontent.com/Lucas-Camilo/TCC/main/images/Logo.png', x=170, y=8, w=30)
        self.pdf.cell(200, 10, txt="PyEmotions", ln=1, align="C")
        self.pdf.ln(20)
        self.pdf.set_font("Arial", size=10)
        self.pdf.multi_cell(200, 10,
                            txt="- Para atender às exigências legais da Lei Geral de Proteção de Dados Pessoais (LGPD) e à Política de Segurança da Informação, informamos que os dados incluídos nessa aplicação, serão utilizados somente para a finalidade específica comprovação da analise das emoções, e para nenhuma outra finalidade, e serão armazenados pelo período que a legislação específica assim o exigir e de acordo com a política interna de ciclo de vida dos dados para atendimento das exigências legais.\n- Não é autorizado realizar print, fotos, vídeos das telas do processo de analise, por se tratar de documento interno , que não pode ser tratado fora do ambiente de trabalho, nem deve ser divulgado,  podendo causar danos tanto à imagem e reputação da empresa quanto a de terceiros, em caso de descumprimento dessa normativa haverá instauração de devido processo administrativo e as devidas sanções cabíveis.",
                            align="L")
        self.pdf.set_font("Arial", size=15)
        self.pdf.ln(15)
        #
        self.pdf.cell(200, 10, txt="Raiva:{}{}%".format(" " * 30, self.resultadoFinal['anger'], ), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Desprezo:{}{}%".format(" " * 24, self.resultadoFinal['contempt']), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Nojo:{}{}%".format(" " * 32, self.resultadoFinal['disgust']), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Medo:{}{}%".format(" " * 31, self.resultadoFinal['fear']), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Felicidade:{}{}%".format(" " * 23, self.resultadoFinal['happiness']), ln=1,
                      align="L")
        #
        self.pdf.cell(200, 10, txt="Tristeza:{}{}%".format(" " * 27, self.resultadoFinal['sadness']), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Surpreza:{}{}%".format(" " * 25, self.resultadoFinal['surprise']), ln=1, align="L")
        #
        self.pdf.cell(200, 10, txt="Neutro:{}{}%".format(" " * 29, self.resultadoFinal['neutral']), ln=1, align="L")
        self.pdf.output("relatoriosPDF/{}.pdf".format(self.nome_arquivo))

    def criaTxt(self):
        f = open("relatoriosTXT/{}".format(self.nome_arquivo), 'w', encoding="utf8")
        f.write("{\n'ResultadoFinal':\n")
        f.write("\t" + str(self.resultadoFinal))
        f.write("\n}")
        f.close()

