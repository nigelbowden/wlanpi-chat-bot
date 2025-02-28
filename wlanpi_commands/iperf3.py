from .command import Command
import os
import subprocess

class Iperf3(Command):
    
    def __init__(self, telegram_object, conf_obj):
        super().__init__(telegram_object, conf_obj)

        self.command_name = "iperf3"
    
    def run(self, args_list):

        IPERF = '/usr/bin/iperf3'
        target_ip = ''
        proto = "tcp"

        # pull off the first arg, which is IP address
        if len(args_list) > 0:
            target_ip = args_list[0]
        
        if len(args_list) > 1:
            proto = args_list[1]
        
        proto_switch = "" # blank = tcp
        if proto == "udp": proto_switch = "-u"

        if target_ip:
            progress_msg = "Runing iperf3 test ({})...".format(proto)
            cmd_string = "{} -i 1 {} -c {} 2>&1".format(IPERF, proto_switch, target_ip) 
            return self._render(self.run_ext_cmd(progress_msg,cmd_string))
        else:
            return self._render("Unable to run test, no IP address passed (syntax : iperf3 &lt;ip_address&gt;)")
