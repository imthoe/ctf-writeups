```
root@[127.0.1.1]:~/ctf/cactuscon/plan# unzip plan.docx 
Archive:  plan.docx
  inflating: [Content_Types].xml     
   creating: _rels/
  inflating: _rels/.rels             
   creating: word/
  inflating: word/fontTable.xml      
   creating: word/_rels/
  inflating: word/_rels/header1.xml.rels  
  inflating: word/_rels/fontTable.xml.rels  
  inflating: word/_rels/document.xml.rels  
   creating: word/theme/
 extracting: word/theme/theme2.xml   
  inflating: word/theme/theme1.xml   
   creating: word/media/
  inflating: word/media/image1.jpg   
  inflating: word/media/image2.png   
  inflating: word/document.xml       
   creating: word/fonts/
  inflating: word/fonts/OpenSans-italic.ttf  
  inflating: word/fonts/OpenSans-bold.ttf  
  inflating: word/fonts/OpenSans-regular.ttf  
  inflating: word/fonts/PTSansNarrow-bold.ttf  
  inflating: word/fonts/PTSansNarrow-regular.ttf  
  inflating: word/fonts/OpenSans-boldItalic.ttf  
  inflating: word/styles.xml         
  inflating: word/numbering.xml      
  inflating: word/settings.xml       
  inflating: word/header2.xml        
  inflating: word/footer1.xml        
  inflating: word/header1.xml        
root@[127.0.1.1]:~/ctf/cactuscon/plan# cd word/theme/
root@[127.0.1.1]:~/ctf/cactuscon/plan/word/theme# file theme2.xml 
theme2.xml: bzip2 compressed data, block size = 900k
root@[127.0.1.1]:~/ctf/cactuscon/plan/word/theme# bzip2 -d theme2.xml 
bzip2: Can't guess original name for theme2.xml -- using theme2.xml.out
root@[127.0.1.1]:~/ctf/cactuscon/plan/word/theme# file theme2.xml.out 
theme2.xml.out: JPEG image data, JFIF standard 1.01, aspect ratio, density 96x95, segment length 16, baseline, precision 8, 334x328, components 3
```

![](theme2.xml.out)
