from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Logs:
    @staticmethod
    def get_logs(
        from_block: int,
        to_block: str,
        address: str,
        topic_0: str = "",
        topic_1: str = "",
        topic_2: str = "",
        topic_3: str = "",
        topic_0_1_opr: str = "",
        topic_1_2_opr: str = "",
        topic_2_3_opr: str = "",
        topic_0_2_opr: str = "",
        topic_0_3_opr: str = "",
        topic_1_3_opr: str = "",
    ):
        """This is an alternative to the native eth_getLogs. An address and/or
        topic_x parameters are required. When multiple topic_x parameters are
        used, the topic_x_y_opr ("and"/"or" operator) is also required.

        **NOTE: Only the first 1000 results are returned.**

        Args:
            from_block (int): Start block of the query.
            to_block (int): End block of the query.
            address (str): Address of the logs.
            topic_0 (str, optional): Topic 0 in the logs. Defaults to "".
            topic_1 (str, optional): Topic 1 in the logs. Defaults to "".
            topic_2 (str, optional): Topic 2 in the logs. Defaults to "".
            topic_3 (str, optional): Topic 3 in the logs. Defaults to "".
            topic_0_1_opr (str, optional): Logical operator between topic 0 and 1. Defaults to "".
            topic_1_2_opr (str, optional): Logical operator between topic 1 and 2. Defaults to "".
            topic_2_3_opr (str, optional): Logical operator between topic 2 and 3. Defaults to "".
            topic_0_2_opr (str, optional): Logical operator between topic 0 and 2. Defaults to "".
            topic_0_3_opr (str, optional): Logical operator between topic 0 and 3. Defaults to "".
            topic_1_3_opr (str, optional): Logical operator between topic 1 and 3. Defaults to "".

        Returns:
            dict: The event logs in a dictionary, including topics and data fields.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_logs(
                        from_block=4993830,
                        to_block=4993832,
                        address="0xe561479bebee0e606c19bb1973fc4761613e3c42",
                        topic_0="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                        topic_0_1_opr="and",
                        topic_1="0x000000000000000000000000730e2065b9daee84c3003c05bf6d2b3a08e55667"
                    )
                )

        Results::

            [
                {
                "address": "0xe561479bebee0e606c19bb1973fc4761613e3c42",
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000730e2065b9daee84c3003c05bf6d2b3a08e55667",
                    "0x000000000000000000000000d7d19938eae260d7f0e0a4c36e665ff4cf4b7acc"
                ],
                "data": "0x000000000000000000000000000000000000000000000000076cd96f53f24b0a",
                "blockNumber": "0x4c3326",
                "timeStamp": "0x602e9ef1",
                "gasPrice": "0x2540be400",
                "gasUsed": "0x1b0f2",
                "logIndex": "0xf7",
                "transactionHash": "0x73844fcfc6beab2e973a897c9573f4d79811b12213ce263045a203e0d3cea90e",
                "transactionIndex": "0xb9"
                }
            ]
        """
        query_string = (
            f"{fields.MODULE}"
            f"{modules.LOGS}"
            f"{fields.ACTION}"
            f"{actions.GET_LOGS}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        if isinstance(from_block, int) or from_block == "latest":
            query_string += (
                f"{fields.FROM_BLOCK}"
                f"{from_block}"
                )
        else:
            raise RuntimeError("Invalid from_block. It must be integer or latest")
        if isinstance(to_block, int) or to_block == "latest":
            query_string += (
                f"{fields.TO_BLOCK}"
                f"{to_block}"
                )
        else:
            raise RuntimeError("Invalid to_block. It must be integer or latest")
        
        if topic_0 is not None:
            query_string += (
                f"{fields.TOPIC_0}"
                f"{topic_0}"
            )
        if topic_1 is not None:
            query_string += (
                f"{fields.TOPIC_1}"
                f"{topic_1}"
            )
        if topic_2 is not None:
            query_string += (
                f"{fields.TOPIC_2}"
                f"{topic_2}"
            )
        if topic_3 is not None:
            query_string += (
                f"{fields.TOPIC_3}"
                f"{topic_3}"
            )
        if topic_0_1_opr == 'and' or topic_0_1_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_0_1_OPR}"
                f"{topic_0_1_opr}"
                )
        if topic_0_2_opr == 'and' or topic_0_2_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_0_2_OPR}"
                f"{topic_0_2_opr}"
                )
        if topic_0_3_opr == 'and' or topic_0_3_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_0_3_OPR}"
                f"{topic_0_3_opr}"
                )
        if topic_1_2_opr == 'and' or topic_1_2_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_1_2_OPR}"
                f"{topic_1_2_opr}"
                )
        if topic_1_3_opr == 'and' or topic_1_3_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_1_3_OPR}"
                f"{topic_1_3_opr}"
                )
        if topic_2_3_opr == 'and' or topic_2_3_opr == 'or':
            query_string+= (
                f"{fields.TOPIC_2_3_OPR}"
                f"{topic_2_3_opr}"
                )
        return query_string
