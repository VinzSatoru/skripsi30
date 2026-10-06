import os
import docx

for f in os.listdir('.'):
    if f.endswith('.docx') or f.endswith('.md'):
        print('FILE:', f)
