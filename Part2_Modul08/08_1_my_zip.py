syms_str = "abc"
nums_tpl = (10, 20, 30, 40)

pairs = [(syms_str[i_elem], nums_tpl[i_elem]) 
         for i_elem in range(len(syms_str))]

