available_steps = ["Transformer",
                   "Premerger",
                   "Business Transformer",
                   "Address Parser",
                   ]

valid_choices = [str(i) for i in range(1, len(available_steps) + 1)]
print(valid_choices)  # todo remove
current_choice = '-'  # Something that will not be inputted, to act as a placeholder
step_script = []

while current_choice != '0':
    if current_choice in valid_choices:
        if current_choice == '1':
            step_script.append("python3 execute_qa/transformer_execute.py")
            print("Enter the transformer path")
            raw_path = input()
            print("Enter the raw path")
            transformer_path = input()
            print("Enter the source id")
            source_id = input()
            print("Enter the parent source id")
            parent_source_id = input()
            print(f"python3 execute_qa/transformer_execute.py -trf {transformer_path} -raw {raw_path} -sid {source_id} "
                  f"- psid {parent_source_id}")
        elif current_choice == '2':
            print('2')
    else:
        print("Select the number of the step to QA")
        for step in available_steps:
            print(f"{available_steps.index(step) + 1}: {step}")
        print("0: Exit Program")

    current_choice = input()