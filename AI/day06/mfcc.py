import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp
sample_rate, sigs = wf.read(
	'../../data/speeches/training/orange/orange01.wav')
mfcc = sf.mfcc(sigs, sample_rate)
print(mfcc.shape)
mp.matshow(mfcc, cmap='jet', fignum='MFCC')
mp.title('MFCC', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Sample', fontsize=14)
mp.tick_params(which='both', top=False,
	labeltop=False, labelbottom=True,
	labelsize=10)
mp.savefig('../../data/orange01.png')
mp.show()
