import io

# clean_line replace tab with | and delete extra spaces from a line.
def clean_line(line):
  return line.replace('\t', '|').replace(' ','')

try: 
  with io.open("datos_data_engineer.tsv", 'r', encoding='utf-16le') as tsv_input: 
    with io.open('output.csv', 'w', encoding='utf-8') as csv_output:
      line = clean_line(tsv_input.readline())
      while line != '':
        if (line.count('|') == 4):
          csv_output.write(line)
          line = clean_line(tsv_input.readline())
        else:        
          end_line = clean_line(tsv_input.readline())
          if end_line != '': #check if there are more lines
            line = line.replace('\n','') + end_line
          else: line = ''
except: print('Error opening file')
