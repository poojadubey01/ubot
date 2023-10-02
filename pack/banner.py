from colorama import init,Fore,Back,Style
init(autoreset=True)
fc=Fore.CYAN
fy=Fore.YELLOW
fm=Fore.MAGENTA
sb=Style.BRIGHT
fr=Fore.RED
fb=Fore.BLUE
def banner():A=f"""
{fr}{sb}
  _____    __    ___               ____ __    
 / ___/__ / /_  / _ )___ ___  ___ / _(_) /____
/ (_ / -_) __/ / _  / -_) _ \\/ -_) _/ / __(_-<
\\___/\\__/\\__/ /____/\\__/_//_/\\__/_//_/\\__/___/                                         
{Style.RESET_ALL}
""";print(A)
def msg():A=f"\n{fc}{fr}[{fy}*{fc}{fr}] {fb}Please be patient, It may take some time to Get Courses for you!{fb} {fr}[{fy}*{fc}{fr}]\n";print(A)
def info():A=f"\n{fc}{fr}[{fy}*{fc}{fr}] {fb}Coded By:{fb} {fr}Ashley {fr}{fy}&{fr} {fr}well300{fr}\n{fc}{fr}[{fy}*{fc}{fr}] {fb}YouTube:{fb}{fr} @CodingWithWell300{fr}\n";print(A)
def end_msg():A=f" \n{fc}{fr}[{fy}*{fc}{fr}] {fb}Thank you for your patience!{fb}\n{fc}{fr}[{fy}*{fc}{fr}] {fb}All Paid Courses for free to enroll are saved in getbenefits.txt{fb}\n{fc}{fr}[{fy}*{fc}{fr}] {fb}Hope to see you again ❤!!{fb}\n";print(A)
if __name__=='__main__':banner();msg();info();end_msg()