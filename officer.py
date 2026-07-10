from officeroperations import officerOperation
from login_activity import loginAactivity

class Officer:
    def __init__(self):
        self.off_oper = officerOperation()
        self.logInAct = loginAactivity()

    def officer_menu(self,officer_id):
        self.officer_id = officer_id 
        Running = True
        while Running == True:
            print("""
                    ==============================
                        DIGITAL EVIDENCE LOCKER
                            OFFICER MENU
                    ==============================
                    1. Add Evidence
                    2. View My Cases
                    3. Search Case
                    4. Search Evidence
                    5. Transfer Evidence
                    6. View Chain of Custody
                    7. Logout""")
            choice = int(input("enter your choice : "))
            
            if choice == 1:
                print("\n========== ADD EVIDENCE ==========\n")

                evidence_id = input("Enter Evidence ID (EV001): ")
                case_id = input("Enter Case ID: ")
                evidence_type = input("Enter Evidence Type: ")
                description = input("Enter Evidence Description: ")
                date_collected = input("Enter Collection Date (YYYY-MM-DD): ")
                collected_by = int(input("enter officer ID: "))
                storage_location = input("Enter Storage Location: ")
                remarks = input("Enter Remarks: ")

                self.off_oper.addEvidence(evidence_id,
                                        case_id,
                                        evidence_type,
                                        description,
                                        date_collected,
                                        collected_by,
                                        storage_location,
                                        remarks)

            elif choice == 2:

                cases = self.off_oper.viewAllCases(officer_id) 

                print(f"{'case_id':<10}{'case_title':<35}{'location':<30}{'status':<10}")
                print("-" * 90)
                for case in cases:
                        print(f"{case[0]:< 10}{case[1]:<35}{case[2]:<30}{case[3]:<10}")  

            elif choice == 3:
                case_id = int(input("Enter the Case ID: "))
                case_details = self.off_oper.searchCase(case_id)

                for case in case_details:
                    print("-" * 50)
                    print(f"Case Title    : {case[0]}")
                    print(f"Crime Type    : {case[1]}")
                    print(f"Incident Date : {case[2]}")
                    print(f"Location      : {case[3]}")
                    print(f"Description   : {case[4]}")
                    print(f"Status        : {case[5]}")
                    print("-" * 50)
                        
            elif choice == 4:  

                print("========== Search Evidence ==========")
                print("""
                        1. Search by Evidence ID
                        2. Search by Case ID
                        3. Search by Evidence Type
                    """)
                choice = int(input("Enter you choice : "))
                
                if choice == 1:
                    evidence_id = input("Enter Evidence ID : ")
                    evidence_details = self.off_oper.searchEvidence(choice,evidence_id)

                    for evidence in evidence_details:

                        print("-" * 50)
                        print(f"case_id           : {evidence[0]}")
                        print(f"evidence_type     : {evidence[1]}")
                        print(f"description       : {evidence[2]}")
                        print(f"date_collected    : {evidence[3]}")
                        print(f"collected_by      : {evidence[4]}")
                        print(f"storage_location  : {evidence[5]}")
                        print(f"status            : {evidence[6]}")
                        print(f"remarks           : {evidence[7]}")
                        print("-" * 50)  

                elif choice == 2:
                    case_id = int(input("Enter case ID: "))
                    evidence_details = self.off_oper.searchEvidence(choice,case_id)

                    for evidence in evidence_details:

                        print("-" * 50)
                        print(f"evidence_id       : {evidence[0]}")
                        print(f"evidence_type     : {evidence[1]}")
                        print(f"description       : {evidence[2]}")
                        print(f"date_collected    : {evidence[3]}")
                        print(f"collected_by      : {evidence[4]}")
                        print(f"storage_location  : {evidence[5]}")
                        print(f"status            : {evidence[6]}")
                        print(f"remarks           : {evidence[7]}")
                        print("-" * 50)                  

                elif choice == 3:
                    evidence_type = input("Enter Evidence Type: ")
                    evidence_details = self.off_oper.searchEvidence(choice,evidence_type)

                    for evidence in evidence_details:

                        print("-" * 50)
                        print(f"evidence_id       : {evidence[0]}")
                        print(f"evidence_type     : {evidence[1]}")
                        print(f"description       : {evidence[2]}")
                        print(f"date_collected    : {evidence[3]}")
                        print(f"collected_by      : {evidence[4]}")
                        print(f"storage_location  : {evidence[5]}")
                        print(f"status            : {evidence[6]}")
                        print(f"remarks           : {evidence[7]}")
                        print("-" * 50)                  

                else:
                    print("invaild choice")

            elif choice == 5:
                print("===========Transfer Evidence==========")

                evidence_id = input("Enter evidence_id(EV001): ")
                from_location = input("Enter current location of evidence: ")
                to_location = input("Enter the location where evidence has been transfering: ")
                transferred_by = self.officer_id
                received_by = input("Enter receiver name ")
                receiver_id = int(input("Enter receiver_id: "))
                reason = input("Enter the reson of transfer: ")

                evidence_transfer_details = self.off_oper.evidence_transfer(evidence_id,
                                                                        from_location,
                                                                        to_location,
                                                                        transferred_by,
                                                                        received_by,
                                                                        receiver_id,
                                                                        reason)
            elif choice == 6:
                evidence_id = input("Enter evidence_id(EV001): ")
                records = self.off_oper.viewChainOfCustody(evidence_id)

                if not records:
                    print("No transfer history found.")
                else:
                    print("\n========== Chain of Custody ==========\n")

                    for record in records:
                        print(f"Transfer ID     : {record[0]}")
                        print(f"Evidence ID     : {record[1]}")
                        print(f"From Location   : {record[2]}")
                        print(f"To Location     : {record[3]}")
                        print(f"Transferred By  : {record[4]}")
                        print(f"Received By     : {record[5]}")
                        print(f"Transfer Date   : {record[6]}")
                        print(f"Reason          : {record[7]}")
                        print("-" * 50)
            elif choice == 7:
                self.logInAct.update_logout(officer_id,)
                print("loging out...............")
                print("Thank you")
                Running = False
    
            else:
                print("invalid choice")
