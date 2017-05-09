import nltk;
from random import randint;

dt = [];
vb = [];
nn = [];
wdt = [];
rb = [];
jj = [];
conj = [];
gmr = [];
ignore = [];

wordlist = [];
textline = [];
repl = [];

frankfilenotSQL = 'words/frank.csv';

verbose = 0;

def getWordTypes(text):
	if not text:
		wordlist.append("ERROR");
	text = nltk.word_tokenize(text);
	words = nltk.pos_tag(text);
	for item, index in words:
		if index == 'DT' or index == 'PRP$':
			dt.append(item);
		if index == 'VB' or index == 'VBD' or index == 'VBG' or index == 'VBN' or index == 'VBP' or index == 'VBZ':
			vb.append(item);
		if index == 'NN' or index == 'NNS' or index == 'NNP' or index == 'NNPS' or index == 'PRP':
			nn.append(item);
		if index == 'WDT':
			wdt.append(item);
		if index == 'RB' or index == 'RBR' or index == 'RBS':
			rb.append(item);
		if index == 'CC' or index == 'IN':
			conj.append(item);
		if index == 'JJ' or index == 'JJR' or index == 'JJS':
			jj.append(item);
		if index == 'IN':
			conj.append(item);
		if index == '?' or index == 'WRB' or ignore == 'MD':
			ignore.append(item);
		if index == ',' or index == '.' or index == '!':
			gmr.append(item);
	if verbose == 1:
		print("");
		print "Determiner", dt;
		print("");
		print "Verb", vb;
		print("");
		print "Noun", nn;
		print("");
		print "WH-Determiner", wdt;
		print("");
		print "Adverb", rb;
		print("");
		print "Adjective", jj;
		print("");
		print "Conjuction", conj;
		print("");
		print "Grammar", gmr;
		print("");
		print "Ignore", ignore;

def addNewNouns(text, n1, n2, n3):
	nouns = [];
	nouns = getTypes(text);
	text = text.replace(nouns[0],n1);
	text = text.replace(nouns[1],n2);
	text = text.replace(nouns[2],n3);
	return text;

def getTypes(text):
	lfb = 0
	wordTypes = getWordTypes(text);

	lfb = nn;
	for value in lfb:
		if (len(value) <= 3):
			lfb.remove(value);

	if (len(lfb) < 3):
		return False;

	if len(lfb) == 0:
		print "FAIL, LFB is NOT a NOUN"
		return False;

	return lfb[0:3];

def updateWordList():
	with open('words/nouns.csv', 'r') as myfile:
	    wordlist=myfile.read().split('\n');
	return wordlist

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getTextFile(filename):
	print "start"
	randomNo = randint(0, 433403);
	print randomNo
	repeat = True
	with open(filename, 'r') as frank:
		print "start openfile"
		frank.seek(randomNo);
		print "seeking"
		while repeat == True:
			print "reading line"
			frank.readline();
			print "assigning readline to local var"
			textline = frank.readline();
			print "starting if to check leng"
			if (len(textline) <= 10 or len(textline) >= 140):
				print "setting types to getTypes vals"
				types = getTypes(textline)
				print "if types is false, restart while"
				if (types != False):
					print "success!"
					outputs = [textline, types];
					repeat = False;
			else:
				print "sentence is too short"
				repeat = True;
		return textline;

#TODO:
#	1. get frank.txt DONE
#	2. get rndm pos in frank DONE
#	3. select a sentence that is 140 chars max with  a lower limit of 10

wordlist = updateWordList();

textwords = ' '.join(wordlist);

#getWordTypes(textwords);

print("");

outputTextFile = getTextFile(frankfilenotSQL);

#print outputTextFile;

print("");

repl.append('table');
repl.append('mug');
repl.append('chair');

print getTypes(outputTextFile);
print "['" + repl[0] + "', '" + repl[1] + "', '" + repl[2] + "']";
print addNewNouns(outputTextFile, repl[0], repl[1], repl[2]);
#print addNewNouns(outputTextFile, 'table', 'mug', 'chair');