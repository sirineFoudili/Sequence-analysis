import random
import tkinter
from tkinter import *
from tkinter import filedialog
from random import  random, choice

def télécharger_fichier():
	fichier=filedialog.askopenfilename(initialdir="/",title="Parcourir",filetypes=(("fasta",'*.fasta'),("All Files","*.*")))
	return fichier

class ADN (object):

	
	def __init__(self, brin, brin2):
		
		"""
		
		CREATION DE LA CHAINE ADN A PARTIR DE DEUX BRINS
		
		"""
		
		##print "creation de l'ADN"
		if brin == None :
			brin = []
		if brin2 == None :
			brin2 = []

		self.brin = brin
		self.brin2 = brin2
		self.taille = len(brin)


	def comp (self, brin):
		"""
		
		Faire le complement d'un brin
		
		"""
		##print "Completer deuxieme brin"
		tab = ["A","C","G","T"]
		tab2 = ["T","G","C","A"]
		brin2=[]
		for i in brin :
			for j in range(0,4):
				if (i==tab[j]):
					brin2.append(tab2[j])
		return brin2
	def comp_affichage(self,brin):
		comp=Toplevel()
		comp.title("Complément inverse")

		tab = ["A","C","G","T"]
		tab2 = ["T","G","C","A"]
		brin2=[]
		for i in brin :
			for j in range(0,4):
				if (i==tab[j]):
					brin2.append(tab2[j])

		com=tkinter.Label(comp)
		com['text']='Le complément inverse = '+''.join(brin2)
		com.pack()

		sauvegarde_fichier('======================== \n Complément inverse : \n'+str(brin2))

		return brin2

		'''
	def valider_champs(fen,champs):
		c=champs.get()
		fen.quit()
		print (c)
		return c
       '''
	def affichRand(self) : 
		'''
		
		pas besoin
		
		'''
		chaine = self.chaineADN()
		self.brin = self.brin2
		chaine = chaine + self.chaineADN()
		self.brin = self.comp(self.brin2)
		
		#print (chaine)
		n=len(chaine)
		return chaine

	def makerandomADN(self,taille):
		"""
		
		Creation d'un ADN aleatoire
		
		"""
		##print "creation d'ADN aleatoire"
		
		self.taille = taille
		brin = []
		tab = ["A","C","G","T"]
		for i in range (0,taille):
			brin.append(choice(tab))
		brin2 = self.comp(brin)
		self.brin = brin
		self.brin2 = brin2
		#self.affichRand() à revoir
		

		
	
	def openfastaADN(self,lien):
		"""
		
		Creation d'un ADN a partir d'un fichier Fasta
		
		"""
		fichier = open(lien,"r")
		liste = []
		for ligne in fichier:
			liste.append(ligne)
		chaine = ''
		i = 1
		n=len(liste)
		
		while ((liste[i][0] != '>') and (i < (n-1) )) :
			liste[i].replace("\n","")
			chaine=chaine+liste[i]
			i=i+1
		ch =''
		for i in range (0,len(chaine)) :
			if ((chaine[i]!='\n') and (chaine[i]!='N')) :
				ch = ch + chaine[i]
		brin =[]
		for j in range(0,len(ch)):
			brin.append(ch[j])
		brin2 = self.comp(brin)
		self.brin = brin 
		self.brin2 = brin2
		self.taille=len(brin)
		#self.validation()
		
		
	def validation(self):
		"""
		
		Verifier la validite d'un ADN
		La fonction retourne True si les deux brin sont complementaires
		Et si la chaine ne contient que des 'A' 'C' 'G' 'T'
		elle retourne False sinon
		
		"""

		"""
		freq=Toplevel()
		freq.title("fréquences des bases nucléiques")
		Adenin=tkinter.Label(freq,text="le nombre d'Adénine dans la chaine est : ")
		A=tkinter.Label(freq)
		A.grid(row='0',column='1')
		Adenin.grid(row='0',column='0')
        """

		val=Toplevel()
        
		val.title( "validité de la chaine" )
		valide=tkinter.Label(val,text="sequence valide")
		#va=tkinter.Label(val)
		#valide.grid(row='1',column='1')
		invalide=tkinter.Label(val,text="sequence invalide")
		#inv=tkinter.Label(val)
		#invalide.grid(row='1',column='1')
		boolean = True
		for i in self.brin :
			if (i!='A') :
				if(i!='C') :
					if (i!='G') :
						if(i!='T') :
							if (i!='N') :
								boolean = False
								print (i)
		#print(self.chaineADN())
		if boolean :
			if (self.brin2 == self.comp(self.brin)) :
				valide.pack()

				sauvegarde_fichier('======================== \n Validité : valide \n')
				return True
				
			else :
				invalide.pack()

				sauvegarde_fichier('======================== \n Validité : invalide \n')
				return False
				
		else :
			invalide.pack()
			#print(self.chaineADN())
            
			sauvegarde_fichier('======================== \n Validité : invalide \n')
			return False

	def frequence_affichage(self):
		"""
		
		La fonction retourne la frequence des bases azotee dans une chaine ADN
		
		"""
		freq=Toplevel()
		freq.title("fréquences des bases nucléiques")
		Adenin=tkinter.Label(freq,text="le nombre d'Adénine dans la chaine est : ")
		A=tkinter.Label(freq)
		A.grid(row='0',column='1')
		Adenin.grid(row='0',column='0')
		Cythosine=tkinter.Label(freq,text="le nombre de Cythosine dans la chaine est : ")
		C=tkinter.Label(freq)
		C.grid(row='1',column='1')
		Cythosine.grid(row='1',column='0')
		Guanine=tkinter.Label(freq,text="le nombre de Guanine dans la chaine est : ")
		G=tkinter.Label(freq)
		G.grid(row='2',column='1')
		Guanine.grid(row='2',column='0')
		Thymine=tkinter.Label(freq,text="le nombre de Thymine dans la chaine est : ")
		T=tkinter.Label(freq)
		T.grid(row='3',column='1')
		Thymine.grid(row='3',column='0')
		n = self.taille
		#tab = [["A",0],["T",0],["C",0],["G",0]]
		tab = {
		"A" :0,
		"C":0,
		"T":0,
		"G":0
		}
		tab["A"]=self.brin.count("A")+self.brin.count("T")
		tab["C"]=self.brin.count("C")+self.brin.count("G")
		tab["T"]=tab["A"]
		tab["G"]=tab["C"]
		A["text"]=tab["A"]
		C["text"]=tab["C"]
		G["text"]=tab["G"]
		T["text"]=tab["T"]

		sauvegarde_fichier('======================== \n Fréquences : \n A : '+str(tab['A'])+' \n T:'+ str(tab['T'])+' \n G:'+ str(tab['G'])+' \n G:'+ str(tab['G'])+'\n')

		return tab
	def frequence(self):
		"""
		
		La fonction retourne la frequence des bases azotee dans une chaine ADN
		
		"""
		n = self.taille
		#tab = [["A",0],["T",0],["C",0],["G",0]]
		tab = {
		"A" :0,
		"C":0,
		"T":0,
		"G":0
		}
		tab["A"]=self.brin.count("A")+self.brin.count("T")
		tab["C"]=self.brin.count("C")+self.brin.count("G")
		tab["T"]=tab["A"]
		tab["G"]=tab["C"]

		return tab

	def assemblage(self,ADNs) :
		brin = []
		for ADN in ADNs : 
			for nucleotide in ADN.brin :
				brin.append(nucleotide)
		self.brin=brin
		self.brin2 = self.comp(brin)
		self.taille=len(brin)

	
	def freqcodons(self) : 
		'''
		
		Pour chercher la frequence des codons on cherche la frequence de succession codon d'initiation - codon stop 
		Afin de faciliter la manipulation on travaille sur des chaines de caractere
		On remplace les codons d'inititation par 'D' et les codons stop par 'F'
		
		'''
		chaine = self.chaineADN()
		self.brin = self.brin2
		chaine = chaine +" -- "+ self.chaineADN()
		self.brin = self.comp(self.brin2)
		
		"""
		
		Transcription manuelle de l'ADN en ARN , en utilise 'X' pour eviter l'ecrasement de donnees
		
		"""
		chaine = chaine.replace('A','U')
		chaine = chaine.replace('T','A')
		chaine = chaine.replace('G','X')
		chaine = chaine.replace('C','G')
		chaine = chaine.replace('X','C')
		"""
		
		On remplace les codons d'initialisation par 'D'
		
		"""
		chaine = chaine.replace('AUG','D')
		chaine = chaine.replace('CUG','D')
		chaine = chaine.replace('UUG','D')
		"""
		
		On remplace les codons stop par 'F'
		
		"""
		chaine = chaine.replace('UGA','F')
		chaine = chaine.replace('UAA','F')
		chaine = chaine.replace('UAG','F')
		#print(chaine)
		n=len(chaine)
		i=0
		codons = 0
		while ((i<n) and (chaine[i] != 'D')):
			i=i+1
		if i<n :
			boolean = True
			while (i<n):
				while((i<n) and boolean ) :
					if chaine[i] =='F' :
						boolean = False
					i=i+1
				if not boolean : 
					codons = codons + 1
				while((i<n) and not boolean ) :
					if chaine[i] =='D' :
						boolean = True
					i=i+1
		frequence=Toplevel()
		frequence.title("fréquences de codons")
		f=tkinter.Label(frequence)
		f['text']=codons
		f.pack()

		sauvegarde_fichier('======================== \n Fréquences des codons : '+str(codons)+'\n')

		return codons




			



	def tauxGC(self):
		"""
		
		La fonction calcule la frequence des liaisons C-G
		et retourne en pourcentage son Taux 
		
		"""
		##print "Calcul du taux de GC"
		Taux=Toplevel()
		Taux.title("Le taux de GC")
		tab = self.frequence()
		a=tab["G"]
		n=self.taille
		taux = (float(a*100)/n)
		t=tkinter.Label(Taux)
		t['text']='Le taux de GC = '+str(taux)+'%'
		t.pack()

		sauvegarde_fichier('======================== \n Taux de GC : '+str(taux)+'%'+'\n')

		return taux
	
	def chaineADN(self) :
		chaineadn=''
		for i in self.brin :
			chaineadn= chaineadn + i
		return chaineadn
	

class ARN (object):
		
	def __init__(self, brin):
		"""
		
		CREATION DE LA CHAINE ARN A PARTIR D'UN SEUL BRIN
		
		"""
		##print "creation de l'ARN"
		if brin == None :
			brin = []

		self.brin = brin
		self.taille = len(brin)

	def transcription(self,adn) :
		"""
		
		La fonction cree une chaine a partir de la transcription d'ADN
		
		"""
		m1="Transcription de l'ADN en ARN \n"
		brin = adn.brin
		tab = ["A","C","G","T"]
		tab2 = ["U","G","C","A"]
		brin2=[]
		
		for i in brin :
			for j in range(0,4):
				if (i==tab[j]):
					brin2.append(tab2[j])
		self.brin = brin2
		self.taille = len(brin)
		arn=Toplevel()
		arn.title("Transcription en ARN")
		ARN=tkinter.Label(arn)
		ARN["text"]=adn.chaineADN()+"\n" + "=" +"\n" +self.chaineARN()
		ARN.pack()

		sauvegarde_fichier('======================== \n Transcription en ARN : '+self.chaineARN()+'\n')

	def chaineARN(self):
		chainearn=''
		for i in self.brin :
			chainearn= chainearn + i
		return chainearn
	def intron(self):
		intron=Toplevel()
		intron.title("Introns")
		i=tkinter.Label(intron,text="Veuillez télécharger le fichier contenant les introns :")
		introns=télécharger_fichier()

		sauvegarde_fichier("======================== \n Téléchargement de l'intron: "+introns+'\n')

		return introns	

	
	def epissage(self,lien):
		"""
		
		Creation d'un ADN a partir d'un fichier Fasta
		
		"""
		Epissage=Toplevel()
		Epissage.title("Episssage")

		fichier = open(lien,"r")
		liste = []
		for ligne in fichier:
			liste.append(ligne)
		
		i = 1
		n=len(liste)
		introns = []
		while (i < n) :
			chaine = ''
			while ((i < n-1) and (liste[i][0] != '>')) :
				liste[i].replace("\n","")
				chaine=chaine+liste[i]
				i=i+1
				ch =''
				for i in range (0,len(chaine)) :
					if ((chaine[i]!='\n') and (chaine[i]!='N')) :
						ch = ch + chaine[i]
				intron =''
				for j in range(0,len(ch)):
					intron = intron + ch[j]
				introns.append(intron)
			i=i+1
		arn=self.chaineARN()
		for intron in introns :
			arn = arn.replace(intron,'')
		brin =[]
		for i in range (0,len(arn)):
			brin.append(arn[i])
		self.brin=brin
		self.taille=len(self.brin)

		e=tkinter.Label(Epissage)
		e['text']="Le résultat de l'épissage : "+self.chaineARN()
		e.pack()

		sauvegarde_fichier("======================== \n Epissage: "+self.chaineARN()+'\n')
		
class aminoacid (object):
	
	"""
		
	La classe des acides amines necessite deux ditionnaires
	Le premier dictionnaire 'aminodict' sert a reconnaitre quel acide a-t-on lors de synthese des proteines a parti d'un codon de 3 nucleotides
	Le deuxieme dictionnaire 'aminopoids' sert a la masse molaire de chaque acide amine
	
	"""
	aminodict = {
		'UUU':'Phe',	
		'UCU':'Ser', 
		'UAU':'Tyr',	
		'UGU':'Cys',	
		'UUC':'Phe',	
		'UCC':'Ser',	
		'UAC':'Tyr',		
		'UGC':'Cys',	
		'UUA':'Leu',	
		'UCA':'Ser',	
		'UAA':'Stop',	
		'UGA':'Stop',
		'UUG':'Leu',	
		'UCG':'Ser',	
		'UAG':'Stop', 	
		'UGG':'Trp',
		'CUU':'Leu',	
		'CCU':'Pro',	
		'CAU':'His',		
		'CGU':'Arg',
		'CUC':'Leu',	
		'CCC':'Pro',	
		'CAC':'His',		
		'CGC':'Arg',
		'CUA':'Leu',	
		'CCA':'Pro',	
		'CAA':'Gln',		
		'CGA':'Arg',
		'CUG':'Leu',	
		'CCG':'Pro',	
		'CAG':'Gln',		
		'CGG':'Arg',
		'AUU':'Ile',	
		'ACU':'Thr',	
		'AAU':'Asn',		
		'AGU':'Ser',
		'AUC':'Ile',	
		'ACC':'Thr',	
		'AAC':'Asn',		
		'AGC':'Ser',
		'AUA':'Ile',	
		'ACA':'Thr',	
		'AAA':'Lys',		
		'AGA':'Arg',
		'AUG':'Met',  	
		'ACG':'Thr',	
		'AAG':'Lys',		
		'AGG':'Arg',
		'GUU':'Val',	
		'GCU':'Ala',	
		'GAU':'Asp',		
		'GGU':'Gly',
		'GUC':'Val',	
		'GCC':'Ala',	
		'GAC':'Asp',		
		'GGC':'Gly',
		'GUA':'Val',	
		'GCA':'Ala',	
		'GAA':'Glu',		
		'GGA':'Gly',
		'GUG':'Val',	
		'GCG':'Ala',	
		'GAG':'Glu',		
		'GGG':'Gly',
	}

	aminopoids = {
		'Ala':89.1	,
		'Arg':174.2 ,
		'Asn':132.1 ,
		'Asp':133.1 ,
		'Cys':121.2 ,
		'Glu':147.1 ,
		'Gln':146.2 ,
		'Gly':75.1 ,
		'His':155.2 ,
		'Ile':131.2 ,
		'Leu':131.2 ,
		'Lys':146.2 ,
		'Met':149.2 ,
		'Phe':165.2 ,
		'Pro':115.1 ,
		'Ser':105.1 ,
		'Thr':119.1 ,
		'Trp':204.2 ,
		'Tyr':181.2 ,
		'Val':117.1 ,
	}

	def __init__(self, codon) :
		"""
		
		Creation d'un acide amine a partir d'un codon de trois nucleotides
		On utilise le dictionnaire aminodict lors de la creation
		
		"""
		##print "creation de l'acide amine"
		self.name = self.aminodict[codon]
		self.poids = self.aminopoids[self.name]
		
		

class proteine (object):
	
	def __init__(self, name, chaine):
		"""
		
		Creation d'une proteine a partir d'une chaine d'acides amines
		
		"""
		##print "creation de la proteine"
		
		if chaine == None :
			chaine = []
		self.name=name

		self.chaine = chaine
		self.taille = len(chaine) 
		poids = 0
		for acid in chaine :
			poids =  poids + acid.poids
		poids = poids - 18*(self.taille - 1)
		self.poids = poids




	def synthese (self,name,arn):
		"""
		
		Synthese d'une proteine par la traduction d'un ARN messager 
		
		"""
		##print "Synthese de la proteine"
		brin = arn.brin
		n = arn.taille
		##print (n)
		boolean = False
		chaine=[]
		i=0
		protéine=Toplevel()
		protéine.title('Transcription en proteines')
		m1="Detection du codon d'initiation"
		while ((i<(n-2)) and (boolean is not True)):
			###print i
			A=brin[i]
			B=brin[i+1]
			C=brin[i+2]
			codon = A+B+C
			if ((codon=='AUG') or (codon=='CUG') or (codon=='UUG')):
				boolean = True
				acid=aminoacid(codon)
				chaine.append(acid)
			i=i+1
		m2="Fin de la premiere boucle"
		i=+2
		if (boolean is True) :
			m3="Codon de d'initiation trouve"
		else :
			m3="Codon non trouve"
		while ((i<(n-2)) and (boolean is True)):
			A=brin[i]
			B=brin[i+1]
			C=brin[i+2]
			codon = A+B+C
			if ((codon=='UAA') or (codon=='UGA') or (codon=='UAG')):
				boolean = False
				m4="Codon Stop"
			else :
				acid=aminoacid(codon)
				chaine.append(acid)
			i=i+3
		if (chaine==[]) :
			''' Chaine vide , Synthese non effectuee '''
			m5="La synthese de la proteine n'a pas pu etre faite a partir de l'ARN messager"
			self.chaine=chaine
			self.name="proteine vide"
			self.poids=0
			self.taille = 0
		else :
			m5="La synthese de la proteine a pu etre faite avec succes"
			self.chaine=chaine
			self.taille = len(chaine)
			self.name=name
			poids = 0
			for acid in chaine :
				poids =  poids + acid.poids
				
			''' On soustrait le poids de (n-1) mollecules de H20  '''
			poids = poids - 18*(self.taille - 1)
			self.poids = poids
			prot=tkinter.Label(protéine)
			message="La synthèsse de l'ARN messager donne la proteine="+"\n"+self.chainePRO()
            #message=m1+m2+m3+m4+m5+"La synthèsse de l'ARN messager donne la proteine="+"\n"+self.chainePRO()
			#print(message)
			prot['text']=message
			prot.pack()

			sauvegarde_fichier("======================== \n Synthèse de la protéine: "+self.chainePRO()+'\n')
	def chainePRO(self):
		chainepro ='-'
		for i in self.chaine :
			chainepro= chainepro + i.name +"-"
		return chainepro
	def poid(self):
		poid=Toplevel()
		poid.title("Masse protéique")
		p=tkinter.Label(poid)
		p['text']='La masse protéique = '+str(self.poids)
		p.pack()

		sauvegarde_fichier("======================== \n Masse protéique = "+str(self.poids)+'\n')
		'''
	def Affichage_protéine(self,name,arn):
		self.synthese(name,arn)
		self.chainePRO()
		print(self.chainePRO())
		'''
def deuxieme_page(adn,app):
	chaine=Toplevel()

	c=tkinter.Label(chaine,text="Donnez la longueur de la chaine ?")
	c.grid(row='0',column='0')

	champs=tkinter.Entry(chaine)
	champs.grid(row='0',column='1')
	
	
	valider=tkinter.Button(chaine,text="valider",command=lambda: makeADN(app,adn,int(champs.get())))

	valider['bg']='grey'
	valider.grid(row='2',column='0')
	
	
	
def makeADN(app,adn,taille):


	adn.makerandomADN(taille)
	text=tkinter.Label(app,text="votre chaine d'ADN : ",font='times 16')
	

	text['fg']='red'
	text['bg']= 'white'
	text.place(x=30,y=200)

	chaine=tkinter.Label(app)

	chaine['text']=' '
	chaine.place(x=250,y=200)

	chaine['text']=adn.chaineADN()
	chaine.place(x=250,y=200)



	sauvegarde_fichier('======================== \n Chaine : '+adn.chaineADN()+'\n')

def troisieme_page(adn,app):
	adn.openfastaADN(télécharger_fichier())
	text=tkinter.Label(app,text="votre chaine d'ADN : ",font='times 16')
	text['fg']='red'
	text['bg']= 'white'
	text.place(x=30,y=200)
	chaine=tkinter.Label(app)
	chaine['text']=adn.chaineADN()
	chaine.place(x=250,y=200)

	sauvegarde_fichier('======================== \n Chaine : '+adn.chaineADN()+'\n')

def sauvegarde_fichier(commande):
	with open ('./historique.txt','a+') as file:
		file.write(commande)
		file.close()

def main() :
	tab=[]
	Adn = ADN(tab,tab)
	chaine=Adn.chaineADN()
	Arn = ARN(tab)
	Protein = proteine("P",tab)
	#introns=Arn.intron()
	#Protein.chainePRO()
	#Protein.synthese("P",Arn)
	app=tkinter.Tk()
	app.geometry('640x480')
	canvas=Canvas(width='640',height='800')
	canvas['bg']='white'

	app.title("analyse d'ADN")
	app['bg']='white'
	#fond=app.image.load('dna.png').convert()
	fond=PhotoImage(file='dna.png')
	canvas.create_image(0,0,image=fond,anchor=NW)	#page principale
	 
	principal=tkinter.Label(app, text="La séquence d'ADN :",font='times 18')
	principal.place(x=30,y=80)
	principal['bg']='white'

	boutton_generer=tkinter.Button(app,text='générer une chaine automatiquement',font='18',command= lambda : deuxieme_page(Adn,app))
	boutton_generer.place(x=250,y=160)
	boutton_generer['bg']='lightgrey'
    

	boutton_fichier=tkinter.Button(app,text='télécharger un fichier',font='18',command= lambda : troisieme_page(Adn,app )) 
	boutton_fichier.place(x=250,y=120)
	boutton_fichier['bg']='lightgrey'


	barre=Frame(app,bg='white')

	b1=tkinter.Button(barre,text='Tester  la validité',font='18',command= lambda:Adn.validation())
	b1.pack(side=LEFT)
	b1['bg']='#53a9bb'
	b2=tkinter.Button(barre,text='Fréquences des bases nucléiques',font='18',command=lambda: Adn.frequence_affichage())
	b2.pack(side=LEFT)
	b2['bg']='#53a9bb'
	b3=tkinter.Button(barre,text='Transcrire en ARN',font='18',command=lambda: Arn.transcription(Adn))
	b3.pack(side=LEFT)
	b3['bg']='#53a9bb'
	b4=tkinter.Button(barre,text='Transcrire en protéine',font='18',command=lambda: Protein.synthese("P",Arn))
	b4.pack(side=LEFT)
	b4['bg']='#53a9bb'
	b5=tkinter.Button(barre,text='Complément inverse',font='18',command=lambda: Adn.comp_affichage(Adn.brin))
	b5.pack(side=LEFT)
	b5['bg']='#53a9bb'
	b6=tkinter.Button(barre,text='Taux de GC',font='18',command=lambda: Adn.tauxGC())
	b6.pack(side=LEFT)
	b6['bg']='#53a9bb'
	b7=tkinter.Button(barre,text='Fréquences de codons',font='18',command=lambda:Adn.freqcodons())
	b7.pack(side=LEFT)
	b7['bg']='#53a9bb'
	b8=tkinter.Button(barre,text='Masse protéique',font='18',command=lambda:Protein.poid())
	b8.pack(side=LEFT)
	b8['bg']='#53a9bb'
	b9=tkinter.Button(barre,text='Epissage',font='18',command=lambda:Arn.epissage(Arn.intron()))
	b9.pack(side=LEFT)
	b9['bg']='#53a9bb'
	#b10=tkinter.Button(barre,text='Assemblage',font='18',command=lambda:Adn.assemblage(Adn))
	#b10.pack(side=LEFT)
	#b10['bg']='#53a9bb'
	quitter=tkinter.Button(barre,text='Quitter',font='18',command=app.quit)
	quitter.pack(side=RIGHT)
	quitter['bg']='red'
	barre.pack(side=TOP,fill=X)
	canvas.pack(fill=BOTH)
	app.mainloop()
	#octopus='C:\Users\USER\Downloads\pseudo_without_product.fa\octopus.fa'
	#introns='C:\Users\USER\Downloads\pseudo_without_product.fa\introns.fa'
	#octopus='fichier.fasta'
	#introns='fichier.fasta'
	#tab = ["A","C","G","T"]
	#tab2 = ["T","G","C","A"]
	#chaine = ADN(tab,tab2)
	#chaine.makerandomADN(1000)
	#print (chaine.freqcodons())
	#chaine.openfastaADN(octopus)
	#print (chaine.chaineADN())
	#arn=ARN([])
	#arn.transcription(chaine)
	#print arn.chaineARN()
	#arn.epissage(introns)
	#pro = proteine("Amir",[])
	#pro.synthese("Amir",arn)
	#print pro.chainePRO()
	#print pro.poids
	




if __name__ == "__main__":
	main()
#barre d'outils
