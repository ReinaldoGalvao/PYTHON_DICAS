SELECT * 
from sl1010
WHERE l1_vend = '3350' 
    AND l1_filial = '43' 
    and l1_storc != 'C' 
    and l1_emissao >= 20210814 
    and l1_emissao <= 20210914;