import numpy as np

def save_csv(field,upsample):
    
x = fields.eng_strain()[0, 1, 1, :, :, -1]; np.savetxt("my_eng_strain2.csv",x,delimiter=","); np.save("my_eng_strain2",x)

y = fields.disp()[0, 1, :, :, -1]; np.savetxt("my_disp2.csv",y,delimiter=","); np.save("my_disp2",y)

xs, ys = fields.coords()[0, 0, :, :, -1], fields.coords()[0, 1, :, :, -1]
np.savetxt("my_xcoor.csv",xs,delimiter=",")
np.savetxt("my_ycoor.csv",ys,delimiter=",")
np.save("my_xcoor",xs)
np.save("my_ycoor",ys)