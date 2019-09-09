import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

image = 'm31_proc.fits'
image_file = fits.open(image)
image_data = image_file[0].data
image_mask = image_file[1].data

head = image_file[0].header["DATE"]
print(head)
head = np.array(repr(image_file[0].header))
print(head)
print(type(head))
np.savetxt("Header_{}.txt".format(image[:-5]), [head], fmt="%s")
print(fits.info(image))

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(image_data, cmap='gray', origin='lower')
plt.title("Primary")
# plt.colorbar()

plt.subplot(122)
plt.imshow(image_mask, cmap='gray', origin='lower')
plt.title("Masked Pixels")

plt.show()
