import pandas as pd

# =============================================
# STEP 1: LOAD THE DATA
# =============================================

# Read the Excel file with two sheets
bank = pd.read_excel('accounting_data.xlsx', sheet_name='Bank')
gl = pd.read_excel('accounting_data.xlsx', sheet_name='GL')

print("✅ Data loaded successfully!")
print(f"📊 Bank Transactions: {len(bank)} rows")
print(f"📊 GL Entries: {len(gl)} rows")
print("-" * 50)

# =============================================
# STEP 2: CLEAN THE DATA (Fix Amount Signs)
# =============================================

# GL amounts are negative (expenses), Bank amounts are positive
# We need to make them match by taking absolute values
bank['Amount'] = bank['Amount'].abs()
gl['Amount'] = gl['Amount'].abs()

# =============================================
# STEP 3: PERFORM THE RECONCILIATION
# =============================================

# Merge on Amount
reconciliation = pd.merge(bank, gl, on='Amount', how='outer', indicator=True)

# Find matches and exceptions
matched = reconciliation[reconciliation['_merge'] == 'both']
exceptions = reconciliation[reconciliation['_merge'] != 'both']

# =============================================
# STEP 4: DISPLAY RESULTS (SAFE VERSION)
# =============================================

print(f"✅ Matched: {len(matched)} transactions")
print(f"⚠️ Exceptions (Need Review): {len(exceptions)} transactions")
print("-" * 50)

if len(exceptions) > 0:
    print("\n⚠️ EXCEPTIONS FOUND (Not in GL):")
    
    # SAFE: Use columns that definitely exist
    if 'Date_x' in exceptions.columns:
        date_col = 'Date_x'
    else:
        date_col = 'Date'
    
    if 'Description_x' in exceptions.columns:
        desc_col = 'Description_x'
    else:
        desc_col = 'Description'
    
    if 'Amount_x' in exceptions.columns:
        amt_col = 'Amount_x'
    else:
        amt_col = 'Amount'
    
    # Print the exceptions
    print(exceptions[[date_col, desc_col, amt_col]].to_string(index=False))
    
    # Check if the $75 unknown transaction exists
    unknown = exceptions[exceptions[amt_col] == 75.0]
    if len(unknown) > 0:
        print("\n📝 Suggested Journal Entry for UNKNOWN TRANSACTION:")
        print("   Dr Suspense Account (9999)  $75.00")
        print("   Cr Bank Account (1000)      $75.00")
        print("   (Pending investigation of unknown vendor)")

print("-" * 50)

# =============================================
# STEP 5: EXPORT TO EXCEL
# =============================================

with pd.ExcelWriter('reconciliation_report.xlsx') as writer:
    matched.to_excel(writer, sheet_name='Matched_Items', index=False)
    exceptions.to_excel(writer, sheet_name='Exceptions_Review', index=False)

print("\n📁 Report saved as 'reconciliation_report.xlsx'")
print("   Open it to see two tabs: Matched_Items and Exceptions_Review")
print("\n✅ RECONCILIATION COMPLETE!")