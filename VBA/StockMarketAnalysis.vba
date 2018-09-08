Sub yearstock():
  'define ws'
  Dim ws as Worksheet

  For each ws in Worksheets 'loop through worksheets'
    ws.Range("I1").value = "Ticker" 'add header'
    ws.Range("J1").value = "Total Stock Volume" 'add header'
    lastrow = ws.Cells(Rows.Count, "A").End(xlUp).Row + 1 'go to last row where there is value, need + 1 to end on empty cell, otherwise for loop won't work '
    Dim StockName as String
    Dim TotalStock as Double
    TotalStock = 0
    Dim SummaryTableRow as integer
    SummaryTableRow = 2

    For i = 2 to lastrow
      If ws.Cells(i+1, 1) <> ws.Cells(i, 1) then 'check if we are still within the same stock, if not then... (<> means not equal to )''
        StockName = ws.Cells(i, 1).value
        TotalStock = TotalStock + ws.Cells(i, 7).value 'adding last volume to current total stock'
        ws.Range("I" & SummaryTableRow).Value = StockName 'print stock name in summary table'
        ws.Range("J" & SummaryTableRow).value = TotalStock 'print total stock next to stock name in summary table'
        SummaryTableRow = SummaryTableRow + 1 'go to next row'
        TotalStock = 0 'reset total stock for next stock name'
        'close_stock = ws.Cells(i, 6).value
        'ws.Range("J" & SummaryTableRow).value = open_stock - close_stock
      Else 'if within same stock...'
        TotalStock = TotalStock + ws.Cells(i, 7).value
        'open_stock = ws.Cells(i, 3).value
      End if
    next i
  next ws
End Sub
