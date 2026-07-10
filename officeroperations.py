from database import DataBase_Connection

class officerOperation:
    def __init__(self):
        self.db = DataBase_Connection()
        self.conn = self.db.connect_db()

    def addEvidence(self, evidence_id, case_id, evidence_type, description, date_collected, collected_by, storage_location, remarks):

        cursor = self.conn.cursor()
        query = """
            INSERT INTO evidence
            (
                evidence_id,
                case_id,
                evidence_type,
                description,
                date_collected,
                collected_by,
                storage_location,
                remarks
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            evidence_id,
            case_id,
            evidence_type,
            description,
            date_collected,
            collected_by,
            storage_location,
            remarks
        )
        cursor.execute(query, values)

        self.conn.commit()
        print("Evidence added successfully ")
        cursor.close()

    def viewAllCases(self, officer_id):
        cursor = self.conn.cursor()
        query = """SELECT case_id,case_title,location,status FROM cases
                    WHERE officer_id = %s"""
        cursor.execute(query, (officer_id,))
        cases = cursor.fetchall()
        cursor.close()
        return cases

    def searchCase(self, case_id):

        cursor = self.conn.cursor()
        query = """SELECT case_title,crime_type,incident_date,location,description,status
                    FROM cases
                    WHERE case_id = %s"""
        cursor.execute(query, (case_id,))
        case_details = cursor.fetchall()
        cursor.close()
        return case_details

    def searchEvidence(self, choice, id):
        cursor = self.conn.cursor()

        if choice == 1:
            query = """
                SELECT case_id, evidence_type, description,
                    date_collected, collected_by,
                    storage_location, status, remarks
                FROM evidence
                WHERE evidence_id = %s
            """
            cursor.execute(query, (id,))
            evidence_details = cursor.fetchall()
            cursor.close()
            return evidence_details

        elif choice == 2:
            query = """
                SELECT evidence_id, evidence_type, description,
                    date_collected, collected_by,
                    storage_location, status, remarks
                FROM evidence
                WHERE case_id = %s
            """
            cursor.execute(query, (id,))
            evidence_details = cursor.fetchall()
            cursor.close()
            return evidence_details

        elif choice == 3:
            query = """
                SELECT evidence_id, evidence_type, description,
                    date_collected, collected_by,
                    storage_location, status, remarks
                FROM evidence
                WHERE evidence_type = %s
            """
            cursor.execute(query, (id,))
            evidence_details = cursor.fetchall()
            cursor.close()
            return evidence_details

    def evidence_transfer(self, evidence_id, from_location, to_location, transferred_by, received_by, receiver_id, reason):

        cursor = self.conn.cursor()
        query = """
            INSERT INTO evidence_transfers
            (
                evidence_id,
                from_location,
                to_location,
                transferred_by,
                received_by,
                receiver_id,
                reason
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            evidence_id,
            from_location,
            to_location,
            transferred_by,
            received_by,
            receiver_id,
            reason
        )

        cursor.execute(query, values)
        self.conn.commit()
        print("---------evidence successfully transfer------------")
        cursor.close()

    def viewChainOfCustody(self, evidence_id):

        cursor = self.conn.cursor()

        query = """
            SELECT transfer_id,
                evidence_id,
                from_location,
                to_location,
                transferred_by,
                received_by,
                transfer_date,
                reason
            FROM evidence_transfers
            WHERE evidence_id = %s
            ORDER BY transfer_date
        """

        cursor.execute(query, (evidence_id,))
        records = cursor.fetchall()

        cursor.close()
        return records