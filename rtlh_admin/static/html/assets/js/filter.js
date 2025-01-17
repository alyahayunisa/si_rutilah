<script>
    function filterData(event) {
        event.preventDefault(); // Hindari refresh halaman
        
        const startDate = document.getElementById('start_date').value;
        const endDate = document.getElementById('end_date').value;
        
            if (!startDate || !endDate) {
                alert("Silakan pilih periode tanggal!");
                return;
            }
        
            // Fetch data dari backend dengan filter tanggal
            fetch(`/filter-data?start_date=${startDate}&end_date=${endDate}`)
                .then(response => response.json())
                .then(data => {
                    const tableBody = document.getElementById('dataTable');
                    tableBody.innerHTML = ''; // Kosongkan tabel
        
                    // Tambahkan baris data baru
                    data.forEach((item, index) => {
                        const row = `
                            <tr>
                                <td>${index + 1}</td>
                                <td>${item.tgl_input}</td>
                                <td>${item.nama_kk}</td>
                            </tr>`;
                        tableBody.innerHTML += row;
                    });
                })
                .catch(error => console.error('Error:', error));
        }
</script>