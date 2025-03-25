import traceback

def main():
    try:
        with open("diary.txt", "a") as file:
            first_input = True  

            while True:
                prompt = "What happened today? " if first_input else "What else? "
                entry = input(prompt).strip()  

                if entry.lower() == "done for now":
                    file.write("done for now\n")
                    break  

                file.write(entry + "\n")
                first_input = False  

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}' for trace in trace_back]

        print(f"Exception type: {type(e).__name__}")
        if str(e):
            print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")

if __name__ == "__main__":
    main()
