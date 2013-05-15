from ctypes import cdll, c_char_p, c_double, c_int, c_uint, c_void_p
from ctypes.util import find_library

import os

class FluidHandle():
    ''' Creates a handle to the FluidSynth library. A instance of this class can be used the same
    way any real library handle to FluidSynth can be used. It "implements" all necessary 
    FluidSynth functions.
    
    This class is inspired by the bindings from pyFluidSynth by Whitehead and pyfluidsynth by 
    MostAwesomeDude.
    
    Member:
    handle -- The raw library handle. 
    library_path -- The path of the loaded library (string).
    '''
    
    def __init__( self, library_path = None ):
        self.handle = self.load_library( library_path )
        
        # From settings.h
        self.new_fluid_settings = self.handle.new_fluid_settings
        self.new_fluid_settings.argtypes = ()
        self.new_fluid_settings.restype = c_void_p
        
        self.delete_fluid_settings = self.handle.delete_fluid_settings
        self.delete_fluid_settings.argtypes = (c_void_p,)
        self.delete_fluid_settings.restype = None
        
        self.fluid_settings_get_type = self.handle.fluid_settings_get_type
        self.fluid_settings_get_type.argtypes = (c_void_p, c_char_p)
        self.fluid_settings_get_type.restype = c_int
        
        self.fluid_settings_getnum = self.handle.fluid_settings_getnum
        self.fluid_settings_getnum.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getnum.restype = c_int
        
        self.fluid_settings_getint = self.handle.fluid_settings_getint
        self.fluid_settings_getint.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getint.restype = c_int
        
        self.fluid_settings_getstr = self.handle.fluid_settings_getstr
        self.fluid_settings_getstr.argtypes = (c_void_p, c_char_p, c_void_p)
        self.fluid_settings_getstr.restype = c_int
        
        self.fluid_settings_setnum = self.handle.fluid_settings_setnum
        self.fluid_settings_setnum.argtypes = (c_void_p, c_char_p, c_double)
        self.fluid_settings_setnum.restype = c_int
        
        self.fluid_settings_setnum = self.handle.fluid_settings_setnum
        self.fluid_settings_setint.argtypes = (c_void_p, c_char_p, c_int)
        self.fluid_settings_setint.restype = c_int
        
        self.fluid_settings_setstr = self.handle.fluid_settings_setstr
        self.fluid_settings_setstr.argtypes = (c_void_p, c_char_p, c_char_p)
        self.fluid_settings_setstr.restype = c_int
        
        # From synth.h
        self.new_fluid_synth = self.handle.new_fluid_synth
        self.handle.new_fluid_synth.argtypes = (c_void_p,)
        self.handle.new_fluid_synth.restype = c_void_p
        
        self.delete_fluid_synth = self.handle.delete_fluid_synth
        self.handle.delete_fluid_synth.argtypes = (c_void_p,)
        self.handle.delete_fluid_synth.restype = None
        
        self.fluid_synth_sfload = self.handle.fluid_synth_sfload
        self.handle.fluid_synth_sfload.argtypes = (c_void_p, c_char_p, c_int)
        self.handle.fluid_synth_sfload.restype = c_int
        
        self.fluid_synth_sfreload = self.handle.fluid_synth_sfreload
        self.handle.fluid_synth_sfreload.argtypes = (c_void_p, c_uint)
        self.handle.fluid_synth_sfreload.restype = c_int
        
        self.fluid_synth_sfunload = self.handle.fluid_synth_sfunload
        self.handle.fluid_synth_sfunload.argtypes = (c_void_p, c_uint, c_int)
        self.handle.fluid_synth_sfunload.restype = c_int
        
        self.fluid_synth_noteon = self.handle.fluid_synth_noteon
        self.handle.fluid_synth_noteon.argtypes = (c_void_p, c_int, c_int, c_int)
        self.handle.fluid_synth_noteon.restype = c_int
        
        self.fluid_synth_noteoff = self.handle.fluid_synth_noteoff
        self.handle.fluid_synth_noteoff.argtypes = (c_void_p, c_int, c_int)
        self.handle.fluid_synth_noteoff.restype = c_int
        
        self.fluid_synth_cc = self.handle.fluid_synth_cc
        self.handle.fluid_synth_cc.argtypes = (c_void_p, c_int, c_int, c_int)
        self.handle.fluid_synth_cc.restype = c_int
        
        self.fluid_synth_pitch_bend = self.handle.fluid_synth_pitch_bend
        self.handle.fluid_synth_pitch_bend.argtypes = (c_void_p, c_int, c_int)
        self.handle.fluid_synth_pitch_bend.restype = c_int
        
        self.fluid_synth_pitch_wheel_sens = self.handle.fluid_synth_pitch_wheel_sens
        self.handle.fluid_synth_pitch_wheel_sens.argtypes = (c_void_p, c_int, c_int)
        self.handle.fluid_synth_pitch_wheel_sens.restype = c_int
        
        self.fluid_synth_program_change = self.handle.fluid_synth_program_change
        self.handle.fluid_synth_program_change.argtypes = (c_void_p, c_int, c_int)
        self.handle.fluid_synth_program_change.restype = c_int
        
        self.fluid_synth_bank_select = self.handle.fluid_synth_bank_select
        self.handle.fluid_synth_bank_select.argtypes = (c_void_p, c_int, c_int)
        self.handle.fluid_synth_bank_select.restype = c_int

    def load_library( self, library_path ):
        ''' Create new FluidSynth handle with given library path. If no specific path is given
        or the file doesn't exist this class will try to find the library based on some basic 
        heuristics. '''
        
        # TODO: Search in current directory.
        if not library_path or not os.path.isfile( library_path ):
            self.library_path = find_library('fluidsynth') or \
                                find_library('libfluidsynth') or \
                                find_library('libfluidsynth-1')
        else:
            self.library_path = library_path
            
        return cdll.LoadLibrary( self.library_path )