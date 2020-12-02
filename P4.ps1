function theGame{
    param([Parameter(Mandatory, ValueFromPipeline)] [string] $num)
    if($num -eq "69"){
        Write-Host ""
        Write-Host "Viste eso?. Si, que habilidad."
    } else {
        Write-Host ""
        Write-Host "Uy, casi le atinabas"
    }
}

Read-Host "Number" | theGame