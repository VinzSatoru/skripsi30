$word = New-Object -ComObject Word.Application -ErrorAction SilentlyContinue
if ($word) {
    Write-Output "Word COM is available"
    $word.Quit()
} else {
    Write-Output "Word COM is not available"
}
