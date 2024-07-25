import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelBinarizer
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_selector, make_column_transformer

# from sklearn.pipeline import FeatureUnion
# from sklearn.compose import ColumnTransformer
# from sklearn.ensemble import IsolationForest
# from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.model_selection import train_test_split

from data_transformer import CombinedAttributeAdder

class HousingDataPrepper:
    def __init__(self, data) -> None:
        self.housing = data

    def fillAndDrop(self, use_book=True):
        # TODO: Get back to this later
        # Dont know what this does but just trying it out since it was added as part of the notebook
        # isolation_forest = IsolationForest(random_state=42)
        # outlier_pred = isolation_forest.fit_predict(housing_num)

        # Selct the number types and fill in median values for missing NaN
        # values
        num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy="median")),
            ('attrib_adder', CombinedAttributeAdder()),
            ('scaler', StandardScaler())
        ])

        cat_pipeline_book = Pipeline([
            'label_binarizer', LabelBinarizer()
        ])
        cat_pipeline_pynb = Pipeline([
            ('simple_imputer', SimpleImputer(strategy="most_frequent")),
            ('one_hoit_encoder', OneHotEncoder())
        ])

        cat_pipeline = cat_pipeline_book if use_book else cat_pipeline_pynb

        preprocessing = make_column_transformer(
            (num_pipeline, make_column_selector(dtype_include=np.number)),
            (cat_pipeline, make_column_selector(dtype_include=object))
        )
        preprocessed_hosuing = preprocessing.fit_transform(self.housing)

        X = preprocessed_hosuing.