#definicao dos dados e interfaces da aplicacao
from abc import ABCMeta, abstractmethod, abstractproperty
class IGen:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_rand(self):
        """gera num"""
        
        
from IPython.display import HTML, display #pra printar a tabela
class MyCSVs:
    def __init__(self,file_name,):
        classes = 8
        myf = open(file_name,'r')
        linhas = [l.replace('\n','').strip() for l in myf.readlines()]
        linhas = [l for l in linhas if len(l)!=0 and l[0]!='#']
        myf.close()
        self.entradas = [col.strip() for col in linhas[0].split(',')]
        self.amostras = dict()
        [self.amostras.update({en:[]}) for en in self.entradas]
        for l in [l.split(',') for l in linhas[1:]]:
            for am,col in zip(self.entradas,l):
                try:
                    col = float(col) if col.count('.')==1 else int(col)
                except:
                    # string então
                    col = col.strip()
                self.amostras[am].append(col)
#         print(self.amostras)
    def get_dict(self):
        return self.amostras
    def get_col(self,col):
        return self.amostras[col]
    def get_names(self):
        return list(self.entradas)
    def get_line(self,line,campos=None):
        if campos==None:
            campos = self.entradas
        return tuple([self.amostras[i][line] for i in campos])
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        x = self.a
        if(x >= len(self.amostras[self.entradas[0]]) ):
            raise StopIteration
        self.a += 1
        return self.get_line(x)
    def where(self,campo,valor,campos=None):
        if campos == None:
            campos = self.entradas[1:]
        entries = self.amostras[campo].count(valor)
        st = 0
        r = []
        for i in range(entries):
            pos = self.amostras[campo].index(valor,st)
            st = pos+1
            r+=[self.get_line(pos,campos)]
        return r
#     def get_item(self,col,line):
#         return tuple([self.amostras[self.entradas.index(col)][line] for i in self.entradas])
    def print_html(self):
        corpo = f'<table><tr><th>{"</th><th>".join(self.entradas)}</th></tr>'
        for linha in zip(*[self.amostras[en] for en in self.entradas]):
            corpo+='<tr><td>'+'</td><td>'.join([str(c) for c in linha])+'</td></tr>'
        corpo+='</table>'
#         print(corpo)
        display(HTML(corpo))