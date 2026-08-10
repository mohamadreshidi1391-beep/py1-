#pip install pyscreenshot
# Or: pip install -i https://mirror.abrha.net/repository/pypi/simple pyscreenshot
#pip install pillow 

import pyscreenshot 

image = pyscreenshot.grab() 

image.show() 

image.save("tirotir.png") 


