#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Generic linux daemon base class for python 3.x."""

import sys, os, time, atexit, signal
import copy

from twisted.python import log


class Daemon3:
    """A generic daemon class.

    Usage: subclass the daemon class and override the run() method. """#

    def __init__(self, pidfile):
        self.stopAttempts=0
        self.pidfile = pidfile

    def daemonize(self):
        """Deamonize class. UNIX double fork mechanism."""

        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #1 failed: {0}\n'.format(err))
            sys.exit(1)

        # decouple from parent environment
        os.chdir('/')
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #2 failed: {0}\n'.format(err))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()

        si = open(os.devnull, 'r')
        os.dup2(si.fileno(), sys.stdin.fileno())
        se = open(os.devnull, 'a+')
        os.dup2(se.fileno(), sys.stderr.fileno())
        #
        # NOTE: use nouhup snApiXY.py for file logging.
        #
        logOutputs = 'console'
        #logOutputs = 'noOutput'
        #logOutputs = 'logFile'
        #noConsolOutput = False #True # for NO console diags
        #outputToFile = True

        silent = False
        if silent:

            so = open(os.devnull, 'a+')
            os.dup2(so.fileno(), sys.stdout.fileno())

        elif logOutputs == 'logFile':
        # this needs proper file access rights or so.
        # does not work like this,
            print("USING LOGFILE")
            so = open('SuperNET.log', 'a+')
            os.dup2(so.fileno(), sys.stdout.fileno())

        else:
            pass # standard console output

        atexit.register(self.delpid)

        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write(pid + '\n')


    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        """Start the daemon."""

        # Check for a pidfile to see if the daemon already runs
        try:
            with open(self.pidfile,'r') as pf:

                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if pid:
            message = "pidfile {0} already exists. Daemon already running??\n"
            sys.stderr.write(message.format(self.pidfile))

            try:
                sys.stderr.write("trying to remove pidfile", self.pidfile)

                os.remove(self.pidfile)
            except:

                sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()


    def startUC(self, UC = None):
        """Start the daemon."""#
        # Check for a pidfile to see if the daemon already runs
        try:
            with open(self.pidfile,'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if pid:
            message = "pidfile {0} already exists. Daemon already running??\n"
            sys.stderr.write(message.format(self.pidfile))
            #sys.stdout.write(message.format(self.pidfile))

            try:
                sys.stdout.write("trying to remove pidfile" + self.pidfile)
                os.remove(self.pidfile)

            except Exception as e:
                sys.stdout.write("exiting.err {0}".format(str(e)))
                sys.exit(1)

        # Start the daemon
        self.daemonize()


        self.runUC(UC)



    def stop(self):
        """Stop the daemon."""
        # Get the pid from the pidfile
        try:
            with open(self.pidfile,'r') as pf:
                pid = int(pf.read().strip())
                print(1*"\nstop pid: ", pid)
        except IOError:

            pid = None

        if not pid:
            message = "pidfile {0} does not exist. Daemon not running?\n"
            sys.stderr.write(message.format(self.pidfile))
            return # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                #print(type(signal))
                #print(type(signal.SIGTERM))
                print(signal)
                self.stopAttempts+=1
                print(self.stopAttempts ," tries to stop: ", str(pid), str(signal.SIGTERM))
                time.sleep(0.1)
                if self.stopAttempts > 10:
                    print(self.stopAttempts ," trying kill now: ", str(pid), str(signal.SIGKILL))
                    os.kill(pid, signal.SIGKILL)



        except OSError as err:
            e = str(err.args)
            if e.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err.args))
                sys.exit(1)



    def restart(self):
        """Restart the daemon."""
        self.stop()
        self.start()

    def run(self):
        """You should override this method when you subclass Daemon.

        It will be called after the process has been daemonized by
        start() or restart()."""
