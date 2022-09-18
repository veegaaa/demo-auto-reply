from typing import Any, Dict, Union

import pandas as pd


class Preprocessor:
    """Class for preprocessig data from external APIs."""
    def __init__(self, type: str) -> None:
        self.type = type

    def normalize_api_data(self, data: Dict[str, Any]) -> Union[pd.DataFrame, str]:
        """
        Method for normalizing data from external api to pandas dataframe
        and renaming columns.

        Parameters
        ----------
        data: Dict[str, Any]
            String with raw data like json.

        Returns
        -------
        Union[pd.DataFrame, str]
            Normalized dataframe from raw json.

        Examples
        --------
        >>>PREPROCESSOR.normalize_api_data('{"col_1": [1,2,3], "col_2": [4,5,6]}')
        |col_1|col_2|
           1     4
           2     5
           3     6
        """
        if self.type == 'api':
            result_df = pd.json_normalize(data)
            names = []
            for i in result_df.columns.tolist():  # renaming columns
                buf = i.strip('_')
                buf = buf.replace('._', '__').replace('.', '__').replace('-', '_')
                names.append(buf)
            result_df.columns = names
            return result_df
        else:
            return 'Type of object is not "api".'
