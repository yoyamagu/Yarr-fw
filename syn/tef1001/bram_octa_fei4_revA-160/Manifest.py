# To list file
# ls -1 | xargs -I % echo \"%\",


library = "work"

modules = {
"local" : ["../../../rtl/common","../../../rtl/kintex7","../../../rtl/","../../../ip-cores/kintex7"],
}

files = [
#TOP
"../bram_yarr_tef1001.vhd",
"../../xpressk7/app_pkg.vhd",
"../../xpressk7/app.vhd",
"../tef1001.xdc",
#"../xpressk7-ddr3.xdc",
"../tef1001-fmc-octa.xdc",
"../../xpressk7/xpressk7-timing.xdc",
]




target = "xilinx" 
action = "synthesis" 

syn_device = "xc7k160" 
syn_grade = "-2" 
syn_package = "tfbg676" 
syn_top = "top_level" 
syn_project = "yarr"
syn_tool = "vivado"
