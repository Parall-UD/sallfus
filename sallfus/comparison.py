# -*- coding: utf-8 -*-
from fusion import broveyCPU
from fusion import broveyGPU
from fusion import multiplicativeCPU
from fusion import multiplicativeGPU
from fusion import atrousCPU
from fusion import atrousGPU
from fusion import pcaCPU
from fusion import pcaGPU

def generated_method(method):
    if(method == 'brovey'):
        array_method = [broveyCPU, broveyGPU]
    elif(method == 'multiplicative'):
        array_method = [multiplicativeCPU, multiplicativeGPU]
    elif(method == 'pca'):
        array_method = [pcaCPU, pcaGPU]
    elif(method == 'atrous'):
        array_method = [atrousCPU, atrousGPU]
    else:
         sys.exit('The method is invalid')
    return array_method


def time_comparison(multispectral, panchromatic, method):
    results = dic()
    array_types = ['cpu','gpu']
    if(type(method) != str):
        sys.exit('Methods must be a string')
    method_array = generated_method(method)
    for i in range(len(method_array)):
        result_temp = method_array[i].fusion_images(multispectral, panchromatic)
        results.update({method+'_'+array_types[i] : result_temp})
    return results
