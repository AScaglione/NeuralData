# -*- coding: utf-8 -*-
"""

General class for importing and working with neural data, class is based on dictionary built in class of python. 









Created on Thu Oct 24 16:07:49 2013

@author: Alessandro Scaglione
@contact: alessandro.scaglione@gmail.com
@Version : 0
"""


import numpy as np

class NeuralData(dict):
    
    def __init__(self,**kwargs):
        super(NeuralData, self).__init__(MetaTags={},**kwargs)
        self.FileConstructor()
           
    def __setitem__(self, *args, **kwargs):
        if len(kwargs)>0:
            keys=kwargs.keys()
        else:
            keys=[args[0]]
            
        for kw in keys:
            if (kw != 'Spikes') & (kw != 'Raw') & (kw != 'LFP') & (kw != 'Behavioral') & (kw != 'Analog'):
                print kw,'not implemented yet!!!'
                raise KeyError()
            
        return dict.__setitem__(self, *args, **kwargs)
    

    
    def FileConstructor(self):
        
        """ Create the file structure data class"""
        # Create the MetaTags fields
        self['MetaTags']['SamplingFreq']=int()
        # Defined as optional fields
        self['MetaTags']['FileName']=str()
        self['MetaTags']['FilePath']=str()
        self['MetaTags']['FileExt']=str()
        #    path  = os.path.split(filename)[0]
        #    fname = os.path.split(filename)[1]
        #    fname_,ext = os.path.splitext(fname)
        self['MetaTags']['NumChannels']=int()
        self['MetaTags']['DateTime']=str() #format yy/mm/dd
        
    def BasicConstructor(self):
        
        Base={}
        
  
        #TODO: Mandatory fields without these return errors
          
        Base['SamplingFreq']=int()
          
        # Defined as optional fields
        Base['Type']=str() #for Raw, Spikes, Lfp
        Base['Name']=str() 
        Base['PhysicalChan']=int()
        Base['Bank']=int()
        Base['MaxDigValue']=int()
        Base['MinDigValue']=int()
        Base['MaxAnalogValue']=int() #units in uv
        Base['MinAnalogValue']=int()
        Base['HighFreq']=int()
        Base['LowFreq']=int()
        Base['NumRecords']=int()
        Base['Threshold']=int()
        Base['TimeFirstPoint']=int()
        
        #Data definition
        Base['Waveforms']=np.empty(0,dtype=np.int16)
        Base['TimeStamps']=np.empty(0,dtype=np.int16)
        Base['Units']=np.empty(0,dtype=np.int16)
        Base['Continuous']=np.empty(0,dtype=np.int16)
        
        
        return Base
    
    def AddSpikeChan(self):
        
        if not self.has_key('Spikes'):
            self['Spikes']=[]
            index=0;
        else:
            index=len(self['Spikes'])
        self['Spikes'].append({});
        
        self['Spikes'][index]=self.BasicConstructor()
        self['Spikes'][index].pop('Continuous',None)
        
        
    def AddLFPChan(self):
        
        if not self.has_key('LFP'):
            self['LFP']=[]
            index=0;
        else:
            index=len(self['LFP'])
            
        self['LFP'].append({});
        
        self['LFP'][index]=self.BasicConstructor()
        self['LFP'][index].pop('Waveforms',None)
        self['LFP'][index].pop('TimeStamps',None)
        self['LFP'][index].pop('Units',None)
        
    def AddRawChan(self):
        if not self.has_key('Raw'):
            self['Raw']=[]
            index=0;
        else:
            index=len(self['Raw'])
        
        self['Raw'].append({});
        
        self['Raw'][index]=self.BasicConstructor()
        self['Raw'][index].pop('Waveforms',None)
        self['Raw'][index].pop('TimeStamps',None)
        self['Raw'][index].pop('Units',None)
        
    def AddAnalogChan(self):
        if not self.has_key('Analog'):
            self['Analog']=[]
            index=0;
        else:
            index=len(self['Analog'])
        
        self['Analog'].append({});
        
        self['Analog'][index]=self.BasicConstructor()
        self['Analog'][index].pop('Waveforms',None)
        self['Analog'][index].pop('TimeStamps',None)
        self['Analog'][index].pop('Units',None)
        
    def AddBehavioralChan(self):
        if not self.has_key('Behavioral'):
            self['Behavioral']=[]
            index=0;
        else:
            index=len(self['Behavioral'])
        
        self['Behavioral'].append({});
        
        self['Behavioral'][index]=self.BasicConstructor()
        self['Behavioral'][index].pop('Waveforms',None)
        self['Behavioral'][index].pop('Continuous',None)
        self['Behavioral'][index].pop('Units',None)
        
        
    


    
    


if __name__ == '__main__':
    TestData = NeuralData()
    
    

















        
        
        
    
    
    