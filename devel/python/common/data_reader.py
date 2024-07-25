from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

class DataReader:
    def __init__(self) -> None:
        self.dataset_name = None
        self.url = None
        # TODO: Have to handle multiple dataset types
        # self.dataset_type = None
    
    def read(self):
        if self.dataset_name is None:
            raise ValueError("The name needs to be set")
        
        if self.url is None:
            raise ValueError("The url needs to be set")
        
        if self.dataset_type is None:
            raise ValueError("The dataset_type needs to be set")
        
        os_path = Path("datasets/" + self.dataset_name + ".tgz")
        if not os_path.is_file():
            Path("datasets").mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(self.url, os_path)
            with tarfile.open(os_path) as tarball:
                tarball.extract(path="datasets")
        
        return pd.read_csv(Path("datasets/" + self.dataset_name + ".csv"))
    
class HouseDataReader(DataReader):
    def __init__(self,
                 dn="housing",
                 url="https://github.com/ageron/data/raw/main/housing.tgz") -> None:
        super().__init__()
        self.dataset_name = dn
        self.url = url