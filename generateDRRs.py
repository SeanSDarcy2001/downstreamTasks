from deepdrr import geo, Volume, MobileCArm
from deepdrr.projector import Projector # separate import for CUDA init
import matplotlib.pyplot as plt

volume = Volume.from_nifti('subset0/1.3.6.1.4.1.14519.5.2.1.6279.6001.105756658031515062000744821260.mhd')

carm = MobileCArm()
carm.reposition(volume.center_in_world)

with Projector(volume, carm=carm) as projector:
    carm.move_to(alpha=30, beta=10, degrees=True)
    projection = projector()

plt.imshow(projection, cmap='gray')
plt.show()