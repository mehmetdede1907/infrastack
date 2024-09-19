from workflow import run_sre_workflow

def main():
    # Run the SRE workflow
    result = run_sre_workflow()
    
    print("SRE Assistant Analysis Result:")
    print(result)

if __name__ == "__main__":
    main()