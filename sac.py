import matplotlib.pyplot as plt
import numpy as np
import cCOSMO

plt.style.use("classic")

db = cCOSMO.VirginiaTechProfileDatabase(
    "profiles/VT2005/Sigma_Profile_Database_Index_v2.txt",
    "profiles/VT2005/Sigma_Profiles_v2/",
)
identifiers = ["0438", "0087"]
for iden in identifiers:
    db.add_profile(iden)
    prof = db.get_profile(iden)
    print(prof.name)

COSMO = cCOSMO.COSMO1(identifiers, db)
T = 623.15
z = np.array([0.235, 1 - 0.235])

print(COSMO.get_lngamma(T, z))
