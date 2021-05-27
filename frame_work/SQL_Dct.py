# -*- coding:utf-8 -*-

SQLD = {
    'MEBatch': r'''
declare @success bit 
exec 
cn.CCM_BPBuildWorkMEContractAdjustment '2016/10/1', 0, 0, '00000000-0000-0000-0000-000000000000',@success output 
select @success
    ''',
    'OrderPay': {
        #----拿orderid(OE Basket ku)
        'BasketKU': r'select * from BaseOrderTracker with (nolock) where PurchaserContactID = 20003964929 order by orderdate desc',
        #----拿cashpaymentID
        'cashpaymentID': r"select * from BaseOrderCashPayment with (nolock) where orderid = '63AC9A55-12E5-42A0-A86E-DE14D83277C2'",
        #----假支付
        'fakePayment': r"""
          exec uspCompleteOrderPayment 
        @OrderId = '63AC9A55-12E5-42A0-A86E-DE14D83277C2', 
        @PaymentId = '1333302570'
        """
    }
}
