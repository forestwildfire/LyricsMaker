import markov_python.cc_markov
import fetch_data
import generate_output



f = fetch_data.FetchData("https://www.azlyrics.com/t/taylorswift.html")
l = f.createString()


op1 = generate_output.GenerateOutput(l)
op1.fileOutput("AllLyrics")


M = markov_python.cc_markov.MarkovChain(2)
M.add_string(l.replace("\n"," \\n "))
newLyrics = M.generate_text(150)
op2 = generate_output.GenerateOutput(newLyrics)
op2.consoleOutput()
op2.fileOutput("NewSong")
