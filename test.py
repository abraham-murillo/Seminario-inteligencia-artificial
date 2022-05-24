import math

algoritmoGenetico = [-954.9541186384987, -959.6405322491014, -959.6406627184999, -926.8493245068007, -945.7964281518688, -956.2836353344335, -959.6406627205739, -932.7992237216123, -941.9708284997548, -948.0014888394334, -959.6406626666217, -894.578899990797, -959.300201676495, -959.6406627185117, -937.2749354684256, -955.035128985877, -932.6384584188656, -916.8039079890666, -959.6406627192118, -951.1333092648331]

coloniaHormigas = [-450.41959024172974, -457.0453708434174, -457.0453708434174, -457.0453708434174, -457.0453708434174, -457.0453708434174, -376.536987903445, -450.41959024172974, -376.536987903445, -462.2393003495803, -462.2393003495803, -406.5359154580002, -343.22535385968183, -376.536987903445, -462.2393003495803, -457.0453708434174, -668.5210116931637, -462.2393003495803, -457.0453708434174, -457.0453708434174]

enjambreParticulas = [-716.1057136980021, -716.1057136980021, -716.1057136980021, -716.1057136980021, -716.1804441976909, -716.2769702974879, -716.3446523812563, -716.38347830767, -716.3934372391313, -792.3041698464499, -811.3789887990415, -849.5938970815783, -951.6753835900458, -951.6753835900458, -955.9990759217987, -955.9990759217987, -955.9990759217987, -955.9990759217987, -955.9990759217987, -956.1986922985789]

evolucionDiferencial = [-954.6972407133167, -959.0990390041584, -955.5491394448313, -956.5290127239108, -952.5433724195598, -949.1516977499739, -952.8981660514398, -954.3722298019438, -955.225579575501, -951.8124991986131, -956.4141054928409, -955.7115988091703, -956.4377905314198, -956.035597427425, -957.2589305144068, -950.7839316608688, -955.3357293385712, -952.8698652458513, -956.0525210538513, -950.7960103952084]

inmunesArtificales = [-942.9224558296049, -941.7849394175116, -936.5761908208492, -936.0555539592103, -929.7025345586412, -928.4126330750107, -925.7777373834643, -921.2294234231848, -889.8168130609614, -879.8952202761405, -873.798740387292, -846.5428452149325, -845.8667970681269, -842.0334229542807, -837.3969184581302, -833.7076097200965, -832.5939836300607, -824.5344900883439, -820.7415391466653, -814.7487866402732]

coloniaAbejas= [-733.3073985415226, -799.0890867315592, -704.3869117533642, -756.9200448846718, -796.5319028623844, -894.2410885146287, -699.2726032387242, -896.7514292951088, -699.1588351223199, -743.1659028207564, -846.7562941533033, -797.9120443284507, -836.0997668398913, -872.1446866651229, -841.9584030752915, -874.1360119191752, -767.0792140678489, -729.8192632047619, -766.9150520110247, -821.2470759590894]

def test(a, b): 
  a.sort()
  b.sort()

  l = []
  for i in range(0, len(a)):
    l.append(a[i] - b[i])
  
  l.sort()

  return (len(l) - 2 * l[0] - 1) / math.sqrt(len(l))
    

results = [algoritmoGenetico, coloniaHormigas, enjambreParticulas, evolucionDiferencial, inmunesArtificales, coloniaAbejas]

for i in range(0, len(results)):
  for j in range(0, len(results)):
    if i == j:
      print(0, end=" ")
    else:
      print(test(results[i], results[j]), end="")
  print()


