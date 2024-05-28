import os
import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class MotorBikeTest(rfm.RegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcepath = '.'
    

    # Set the directory where the OpenFOAM tutorial files are located
    tutorial_dir = os.path.join(os.environ['HOME'], 'OpenFOAM', 'openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike', 'tutorials', 'incompressible', 'simpleFoam', 'motorBike')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.executable = f'{os.path.join(self.tutorial_dir, "Allrun")}'
        self.executable_opts = []
        

    run_before('compile')
    def set_executable(self):
        """Set the executable and its options."""
        self.executable = f'{os.path.join(self.tutorial_dir, "Allrun")}'
        self.executable_opts = []

    sanity_function
    def check_log_files(self):
        """Check that the expected log files are present."""
        log_files = [
            'log.blockMesh',
            'log.snappyHexMesh',
            'log.simpleFoam',
            'log.reconstructParMesh',
            'log.reconstructPar',
        ]

        for log_file in log_files:
            assert os.path.exists(os.path.join(self.tutorial_dir, log_file)), f'Log file {log_file} not found'

        return True

    sanity_function
    def check_output(self):
        """Check the output of the simulation."""
        # Add your output checks here
        return True


