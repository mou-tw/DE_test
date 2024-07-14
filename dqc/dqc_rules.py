
def check_dq_EPL_Season(pdf):
    assert pdf['league'].isnull().sum() == 0 , "column league existed null value"
    assert pdf.duplicated().sum() ==0 , "table exists duplicated"
    assert pdf[pdf['winner'].isin(["ERROR",])].empty == True  , "winner column exist ERROR value "
    #add more dqc rules here
    return True