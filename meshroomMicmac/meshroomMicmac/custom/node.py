from meshroom.core import desc
import re
import psutil
import shlex

class MicmacNode(desc.CommandLineNode):
    category = 'Micmac'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
    ]

    def buildCommandLine(self, chunk):
        '''
        Fix command line for MicMac
        '''
        cmdline = desc.CommandLineNode.buildCommandLine(self, chunk)                          # build node command line                    
        cmdline = re.sub('(True|False)', lambda m: str(int(m.group(1) == 'True')), cmdline)   # use 0 / 1 instead of False / True
        cmdline = re.sub('--(\w+)\s', lambda m: '{name}='.format(name=m.group(1)), cmdline)   # use "name=value" instead of "--name value"
        cmdline = re.sub('(\w+=\"\"\s)', lambda m: '', cmdline)                               # remove value with empty string (optional parameter)
        return cmdline
    
    def processChunk(self, chunk):
        try:
            with open(chunk.logFile, 'w') as logF:
                cmd = self.buildCommandLine(chunk)
                projectDir = chunk.node._cmdVars['projectDirectoryValue'].replace('"','') # get project directory from parameter (and remove quotes)
                chunk.status.commandLine = cmd
                chunk.saveStatusFile()
                print(' - commandLine: {}'.format(cmd))
                print(' - logFile: {}'.format(chunk.logFile))
                print(' - projectDir: {}'.format(projectDir))
                chunk.subprocess = psutil.Popen(shlex.split(cmd), stdout=logF, stderr=logF, cwd=projectDir) # execute in project directory

                # store process static info into the status file
                # chunk.status.env = node.proc.environ()
                # chunk.status.createTime = node.proc.create_time()

                chunk.statThread.proc = chunk.subprocess
                stdout, stderr = chunk.subprocess.communicate()
                chunk.subprocess.wait()

                chunk.status.returnCode = chunk.subprocess.returncode

            if chunk.subprocess.returncode != 0:
                with open(chunk.logFile, 'r') as logF:
                    logContent = ''.join(logF.readlines())
                raise RuntimeError('Error on node "{}":\nLog:\n{}'.format(chunk.name, logContent))
        except:
            raise
        finally:
            chunk.subprocess = None