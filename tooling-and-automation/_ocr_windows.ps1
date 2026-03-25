Add-Type -AssemblyName System.Runtime.WindowsRuntime

# Helper function to await WinRT async operations
function Await-Task {
    param([object]$task)
    $null = [System.Threading.Tasks.Task]::Run([System.Func[System.Threading.Tasks.Task]]{
        return [System.WindowsRuntimeSystemExtensions]::AsTask($task)
    }).GetAwaiter().GetResult()
    return $task.GetResults()
}

# Load Windows OCR
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()

if ($null -eq $engine) {
    Write-Host "ERROR: Could not create OCR engine"
    exit 1
}

Write-Host "OCR Engine created successfully. Language: $($engine.RecognizerLanguage.DisplayName)"

$imageDir = "C:\Users\arham\Downloads\QUEENS\Courses\300 Level\_pdf_images"
$images = Get-ChildItem -Path $imageDir -Filter "*.png" | Sort-Object Name

foreach ($img in $images) {
    Write-Host "`n$('='*80)"
    Write-Host "Processing: $($img.Name)"
    Write-Host "$('='*80)"
    
    try {
        $file = [Windows.Storage.StorageFile]::GetFileFromPathAsync($img.FullName)
        $storageFile = Await-Task $file
        
        $stream = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $randomAccessStream = Await-Task $stream
        
        $decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($randomAccessStream)
        $bitmapDecoder = Await-Task $decoder
        
        $softwareBitmap = Await-Task ($bitmapDecoder.GetSoftwareBitmapAsync())
        
        $result = Await-Task ($engine.RecognizeAsync($softwareBitmap))
        
        Write-Host $result.Text
        
        $randomAccessStream.Dispose()
    }
    catch {
        Write-Host "Error processing $($img.Name): $_"
    }
}
