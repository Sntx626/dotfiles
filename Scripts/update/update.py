import os
import time
import json
import snapshot

def ask(question:str, responsesTrue:list=['y','Y','yes','Yes','YES','please'], responsesFalse:list=['n','N','no','No','NO'], use_newline:bool=True) -> bool:
    if use_newline:
        answer = input(f"\n{question} [{responsesTrue[0]}/{responsesFalse[0]}]: ")
    else:
        answer = input(f"{question} [{responsesTrue[0]}/{responsesFalse[0]}]: ")
    if answer in responsesTrue:
        return True
    elif answer in responsesFalse:
        return False
    else:
        print(f"Please answer using only {responsesTrue+responsesFalse}!")
        return ask(question=question, responsesTrue=responsesTrue, responsesFalse=responsesFalse, use_newline=use_newline)

def main() -> None:
    if ask("Do you want to perform a backup (recommended)?", use_newline=False):
        snapshot.take_snapshot()
        if not ask("Proceed with update?"):
            print("Aborting...")
            return

    if ask("Do you want to start the update?"):
        os.system("sudo pacman -Syyu && yay -Syyu")
    
    print("done")

if __name__ == "__main__":
    main()