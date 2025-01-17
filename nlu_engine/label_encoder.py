from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()

class LabelEncoder:
    @staticmethod
    def encode(target_class):
        """
        Encode the labels (ie intents or domains) of the dataframe.
        :param data_df: pandas dataframe
        :return: encoded labels
        """
        label_encoded_y = encoder.fit_transform(target_class)
        return label_encoded_y

    @staticmethod
    def decode(label_encoded_y):
        """
        Decode the labels (ie intents or domains) of the dataframe.
        :param label_encoded_y: encoded labels list
        :return: decoded labels list
        """
        label_decoded_y = encoder.inverse_transform(label_encoded_y)
        return label_decoded_y