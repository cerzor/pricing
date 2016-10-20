INSERT INTO PRICINGAPP.SYM_KR_FINANCE(
       SYMBOL
      ,`YEAR`
      ,REVENUE
      ,GROSS_MARGIN
      ,OPERATING_MARGIN
      ,NET_INCOME
      ,EPS
      ,DIVIDENDS
      ,PAYOUT_RATIO
      ,SHARES
      ,BOOK_VALUE_PS
      ,OPERATING_CF
      ,CAP_SPENDING
      ,FCF
      ,FCF_PS
      ,WORKING_CAPITAL
) VALUES (
   %sym% 
  , %year% 
  ,%rev% 
  ,%gross% 
  ,%opm% 
  ,%net% 
  ,%eps% 
  ,%div%  
  ,%pr%   
  ,%share%   
  ,%bvps%
  ,%opcf% 
  ,%cap%
  ,%fcf%   
  ,%fcfps%  
  ,%wcap%   
)
