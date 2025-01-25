class CustomerSearch
{
    public List<Customer> SearchByCountry(string userInputCountry)
    {
        var countrySpecifiedCustomers = 
            from customer in db.customers
            where customer.Country.Contains(userInputCountry)
            orderby customer.CustomerID ascending
            select customer;

        return  countrySpecifiedCustomers.ToList();
    }

    public List<Customer> SearchByCompanyName(string userInputCompany)
    {
        var companySpecifiedCustomers = 
            from  customer in db.customers
            where  customer.CompanyName.Contains(userInputCompany)
            orderby  customer.CustomerID ascending
            select  customer;

        return companySpecifiedCustomers.ToList();
    }

    public List<Customer> SearchByContact(string userInputContact)
    {
        var contactSpecifiedCustomers = 
            from  customer in db.customers
            where  customer.ContactName.Contains(userInputContact)
            orderby  customer.CustomerID ascending
            select  customer;

        return contactSpecifiedCustomers.ToList();
    }


    public string ExportToCSV(List<Customer> customersDetails)
    {
        StringBuilder customerDetailsCsvFormat = new StringBuilder();

        foreach (var customer in customersDetails)
        {
            customerDetailsCsvFormat.AppendFormat("{0},{1},{2},{3}", customer.CustomerID, customer.CompanyName, customer.ContactName, customer.Country);
            customerDetailsCsvFormat.AppendLine();
        }

        return customerDetailsCsvFormat.ToString();
    }
}
