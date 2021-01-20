select utility_name,month, 
add_months(cast(date_trunc('month', current_date) as date), 11) as twelve_months_out,
datediff(month, month::date, twelve_months_out) as diff
--case when diff=1 then add_months(cast(date_trunc('month', current_date) as date), 10)
--when diff=2 then add_months(cast(date_trunc('month', current_date) as date), 9)
--when diff=2 then add_months(cast(date_trunc('month', current_date) as date), 10)
--end as months_needed

FROM 
(
select *, row_number()over (partition by utility_name order by month::date desc)as rw
from think_glue.csv_genscape_sos_rate_data
where file_date='12/31/2020'
and sos_rate_type='Published'
)
where rw=1

--and sos_rate_type='Published'

select *, date_trunc('month', current_date) as date from analytics.think_invoice
limit 100;

  select *, row_number()over (partition by ap_account_id order by commission_decision, invoice_month desc) as rw
                                from analytics.think_invoices_transposed tit
                                where ap_account_id=1149592
                                
                                select *
                                from think_glue.parquet_daily_costing
                                limit 100;
